import json
import subprocess
from datetime import datetime
from pathlib import Path

from .models import Alert

CHAINSAW_BIN = "C:/tools/chainsaw/chainsaw.exe"


def load_alerts(path: str | Path, origin: str = "") -> list[Alert]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    alerts: list[Alert] = []
    seen: set[tuple[str, str, str]] = set()

    for rec in data:
        doc = rec.get("document", {})
        event = doc.get("data", {}).get("Event", {})
        system = event.get("System", {})

        raw_fields = event.get("EventData") or event.get("UserData") or {}
        fields = raw_fields if isinstance(raw_fields, dict) else {"raw": str(raw_fields)}

        a = Alert(
            alert_id="",
            timestamp=str(rec.get("timestamp", "")),
            host=str(system.get("Computer", "")),
            rule_id=str(rec.get("id", "")),
            rule_title=str(rec.get("name", "")),
            rule_level=str(rec.get("level", "medium")),
            rule_tags=list(rec.get("tags") or []),
            fields=fields,
            source_file=Path(str(doc.get("path", ""))).name,
            origin=origin,
        )

        # Deduplicate: same rule + host + minute
        key = (a.rule_title, a.host, a.timestamp[:16])
        if key in seen:
            continue
        seen.add(key)
        alerts.append(a)

    for i, a in enumerate(alerts, 1):
        a.alert_id = f"A{i:04d}"

    return alerts


def _parse_ts(ts_str: str) -> datetime | None:
    if not ts_str:
        return None
    try:
        return datetime.fromisoformat(ts_str)
    except ValueError:
        return None


def load_events(evtx_path: str | Path) -> list[dict]:
    out = subprocess.check_output(
        [CHAINSAW_BIN, "dump", str(evtx_path), "--json"],
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return json.loads(out)


def one_line(event: dict) -> str:
    ev = event.get("Event", event)
    system = ev.get("System", {})
    data = ev.get("EventData") or ev.get("UserData") or {}
    if not isinstance(data, dict):
        data = {}

    ts = str(
        data.get("UtcTime")
        or system.get("TimeCreated_attributes", {}).get("SystemTime")
        or ""
    )
    eid = str(system.get("EventID", "?"))
    image = str(data.get("Image") or data.get("SourceImage") or "-")

    detail = str(
        data.get("CommandLine")
        or data.get("TargetFilename")
        or data.get("DestinationIp")
        or data.get("TargetImage")
        or data.get("TargetObject")
        or "-"
    )
    return f"{ts} | EventID={eid} | {image} | {detail}".strip()


def attach_context_events(
    alerts: list[Alert],
    raw_dir: str | Path = "data/raw/attack",
    window_seconds: int = 60,
    max_events: int = 5,
) -> list[Alert]:
    event_cache: dict[str, list[dict]] = {}

    for alert in alerts:
        if not alert.source_file:
            continue

        evtx_path = Path(raw_dir) / alert.source_file
        if not evtx_path.exists():
            continue

        if alert.source_file not in event_cache:
            event_cache[alert.source_file] = load_events(evtx_path)

        alert_ts = _parse_ts(alert.timestamp)
        if not alert_ts:
            continue

        neighbors: list[tuple[float, str]] = []
        for raw_ev in event_cache[alert.source_file]:
            ev = raw_ev.get("Event", raw_ev)
            system = ev.get("System", {})
            if str(system.get("Computer", "")) != alert.host:
                continue

            ev_ts_str = system.get("TimeCreated_attributes", {}).get("SystemTime", "")
            ev_ts = _parse_ts(str(ev_ts_str))
            if not ev_ts:
                continue

            diff = abs((ev_ts - alert_ts).total_seconds())
            if 0.001 < diff <= window_seconds:
                neighbors.append((diff, one_line(raw_ev)))

        neighbors.sort(key=lambda item: item[0])
        alert.context_events = [line for _, line in neighbors[:max_events]]

    return alerts
