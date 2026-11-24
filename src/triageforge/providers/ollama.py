import json
import time
from pathlib import Path

import requests
import yaml

BASE = 'http://localhost:11434'
NS = 1_000_000_000
OPTION_KEYS = ('temperature', 'seed', 'num_ctx', 'num_predict', 'top_p', 'top_k', 'repeat_penalty')

def load_yaml(path):
    return yaml.safe_load(Path(path).read_text(encoding='utf-8'))

def settings_for(model, overrides=None):
    # inference.yaml, then this model's overrides from models.yaml, then per-run overrides
    s = dict(load_yaml('config/inference.yaml'))
    for m in load_yaml('config/models.yaml')['models']:
        if m['name'] == model:
            s.update(m.get('overrides') or {})
    s.update(overrides or {})
    return s

def ollama_metrics(r, wall):
    # Ollama reports durations in nanoseconds
    gen = r.get('eval_duration', 0) / NS
    pe = r.get('prompt_eval_duration', 0) / NS
    out_n, in_n = r.get('eval_count', 0), r.get('prompt_eval_count', 0)
    return {
        'wall_seconds': wall,
        'total_seconds': r.get('total_duration', 0) / NS,
        'load_seconds': r.get('load_duration', 0) / NS,
        'prompt_eval_seconds': pe,
        'generation_seconds': gen,
        'prompt_tokens': in_n,
        'generated_tokens': out_n,
        'prompt_tokens_per_second': in_n / pe if pe > 0 else None,
        'generated_tokens_per_second': out_n / gen if gen > 0 else None,
        'in': in_n, 'out': out_n, 'sec': wall,       # short aliases used by the pipeline
    }

def call_local(system, user, model, settings=None):
    s = settings or settings_for(model)
    body = {
        'model': model, 'stream': False, 'keep_alive': s.get('keep_alive', '5m'),
        'options': {k: s[k] for k in OPTION_KEYS if k in s},
        'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}],
    }
    fmt = s.get('format')
    if fmt == 'schema':
        body['format'] = json.loads(Path('config/json_schema_v1.json').read_text(encoding='utf-8'))
    elif fmt:
        body['format'] = fmt
    if 'think' in s:
        body['think'] = s['think']
    started = time.perf_counter()
    resp = requests.post(BASE + '/api/chat', json=body, timeout=300)
    resp.raise_for_status()
    j = resp.json()
    wall = time.perf_counter() - started
    m = ollama_metrics(j, wall)
    msg = j.get('message', {})
    m['done_reason'] = j.get('done_reason')           # 'length' means the output was cut off
    m['thinking_chars'] = len(msg.get('thinking') or '')
    m['model_returned'] = j.get('model')
    return msg.get('content', ''), m
