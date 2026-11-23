from typing import Literal

from pydantic import BaseModel, Field


class Alert(BaseModel):
    alert_id: str
    timestamp: str
    host: str
    rule_id: str = ''         # stable Sigma rule ID (titles can change)
    rule_title: str
    rule_level: str           # low / medium / high / critical
    rule_tags: list[str]      # e.g. ['attack.t1059.001']
    fields: dict              # process, command line, user, etc.
    source_file: str          # which log file it came from (labels only, never shown to the LLM)
    origin: str = ''          # public_attack / lab_benign / lab_atomic
    context_events: list[str] = []   # optional neighbor events (see 4.6)

class TriageVerdict(BaseModel):
    verdict: Literal['likely_malicious', 'suspicious', 'likely_benign']
    confidence: float = Field(ge=0, le=1)
    technique_id: str | None = None
    severity: Literal['low', 'medium', 'high', 'critical']
    evidence: list[str]
    reasoning: str
    recommended_actions: list[str]
    needs_human_review: bool
