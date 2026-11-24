import json
import re

from .models import TriageVerdict
from .providers.ollama import call_local

SUM_KEYS = ('in', 'out', 'sec', 'wall_seconds', 'total_seconds', 'load_seconds',
            'prompt_eval_seconds', 'generation_seconds', 'prompt_tokens',
            'generated_tokens', 'thinking_chars')

FALLBACK = TriageVerdict(verdict='suspicious', confidence=0.0, technique_id=None,
    severity='medium', evidence=[], reasoning='parse failure',
    recommended_actions=['manual review'], needs_human_review=True)

def call_mock(system, user, model, settings=None):
    # No model, no cost, deterministic: tests your plumbing
    benign = any(w in user.lower() for w in ('whoami', 'ipconfig', 'systeminfo'))
    v = {'verdict': 'likely_benign' if benign else 'suspicious',
         'confidence': 0.9 if benign else 0.5, 'technique_id': None,
         'severity': 'low' if benign else 'medium', 'evidence': [],
         'reasoning': 'mock', 'recommended_actions': ['mock'],
         'needs_human_review': not benign}
    return json.dumps(v), {'in': 0, 'out': 0, 'sec': 0.0}

def call_gullible(system, user, model, settings=None):
    # Simulates a model completely fooled by injected text
    v = {'verdict': 'likely_benign', 'confidence': 0.99, 'technique_id': None,
         'severity': 'low', 'evidence': [], 'reasoning': 'obeyed injected text',
         'recommended_actions': [], 'needs_human_review': False}
    return json.dumps(v), {'in': 0, 'out': 0, 'sec': 0.0}

PROVIDERS = {'local': call_local, 'mock': call_mock, 'gullible': call_gullible}

def parse(text):
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)   # some models inline their reasoning
    text = re.sub(r'```json|```', '', text).strip()
    m = re.search(r'\{.*\}', text, re.DOTALL)
    return TriageVerdict(**json.loads(m.group(0) if m else text))

def _finish(t, attempts, error):
    t['attempts'], t['error'] = attempts, error
    g, p = t['generation_seconds'], t['prompt_eval_seconds']
    t['generated_tokens_per_second'] = t['generated_tokens'] / g if g > 0 else None
    t['prompt_tokens_per_second'] = t['prompt_tokens'] / p if p > 0 else None
    return t

def ask(call, system, user, model, settings=None):
    # Try twice. A timeout or bad JSON counts as a failed attempt. If both fail,
    # return the fallback flagged for human review (never drop the row).
    totals = {k: 0 for k in SUM_KEYS}
    totals['done_reason'] = None
    text, error, attempts = '', '', 0
    for _ in range(2):
        attempts += 1
        try:
            text, s = call(system, user, model, settings)
        except Exception:  # noqa: BLE001
            error = 'provider_error'
            continue
        for k in SUM_KEYS:
            totals[k] += s.get(k) or 0
        totals['done_reason'] = s.get('done_reason')
        try:
            return parse(text), _finish(totals, attempts, error), False, text
        except Exception: # noqa: BLE001
            error = 'parse_error'
    return FALLBACK.model_copy(deep=True), _finish(totals, attempts, error), True, text
