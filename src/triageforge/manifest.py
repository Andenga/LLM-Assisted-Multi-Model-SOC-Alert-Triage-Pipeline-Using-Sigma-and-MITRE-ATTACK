import hashlib
import json
import time
from pathlib import Path

import requests

BASE = 'http://localhost:11434'
LOCK = Path('eval/model_bench/locked_models.json')

def sha256_file(path):
    p = Path(path)
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None

def ollama_version():
    return requests.get(BASE + '/api/version', timeout=10).json().get('version')

def model_identity(name):
    tags = requests.get(BASE + '/api/tags', timeout=30).json().get('models', [])
    item = next((m for m in tags if name in (m.get('name'), m.get('model'))), None)
    if item is None:
        raise RuntimeError('model not installed: ' + name + ' (run ollama pull first)')
    show = requests.post(BASE + '/api/show', json={'model': name}, timeout=30).json()
    det, info = show.get('details', {}), show.get('model_info', {})
    return {
        'name': name, 'digest': item.get('digest'), 'size_bytes': item.get('size'),
        'modified_at': item.get('modified_at'), 'family': det.get('family'),
        'parameter_size': det.get('parameter_size'),
        'quantization': det.get('quantization_level'),
        'native_context': next((v for k, v in info.items() if k.endswith('.context_length')), None),
        'capabilities': show.get('capabilities', []),
        'license_head': (show.get('license') or '')[:400],
    }

def loaded_memory(name):
    # call right after a request, while the model is still loaded
    ps = requests.get(BASE + '/api/ps', timeout=10).json().get('models', [])
    m = next((x for x in ps if name in (x.get('name'), x.get('model'))), None)
    return {'memory_bytes': m.get('size'), 'vram_bytes': m.get('size_vram')} if m else {}

def unload(name):
    requests.post(BASE + '/api/generate', json={'model': name, 'keep_alive': 0}, timeout=60)
    time.sleep(2)

def check_lock(identity):
    # refuse to run if this model's digest differs from the locked one
    if not LOCK.exists():
        return
    locked = json.loads(LOCK.read_text(encoding='utf-8'))['models'].get(identity['name'])
    if locked and locked['digest'] != identity['digest']:
        raise RuntimeError('DRIFT: ' + identity['name'] + ' digest changed from '
                           + str(locked['digest'])[:12] + ' to ' + str(identity['digest'])[:12]
                           + '. Treat it as a new model version (see Stage 10C.3).')
