import json
from triageforge.detect import load_alerts   # must dedup inside, per Part 3.5

SETS = [("public_attack", "data/alerts/attack_alerts.json"),
        ("lab_benign",    "data/alerts/benign_alerts.json")]
        # later: ("lab_atomic", "data/alerts/atomic_alerts.json")

MAX_PER_RULE = 20   # stops one noisy rule from filling a whole class

alerts, dropped = [], 0
for origin, path in SETS:
    seen = {}
    for a in load_alerts(path):
        seen[a.rule_title] = seen.get(a.rule_title, 0) + 1
        if seen[a.rule_title] > MAX_PER_RULE:
            dropped += 1
            continue
        d = a.model_dump()
        d["origin"] = origin
        alerts.append(d)

for i, d in enumerate(alerts, 1):
    d["alert_id"] = f"A{i:04d}"

with open("data/alerts/all_alerts.jsonl", "w", encoding="utf-8") as f:
    for d in alerts:
        f.write(json.dumps(d) + "\n")
print(len(alerts), "alerts written;", dropped, "dropped by per-rule cap")