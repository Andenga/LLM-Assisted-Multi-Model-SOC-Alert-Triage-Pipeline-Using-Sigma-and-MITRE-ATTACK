import json
from collections import Counter

import yaml


def load_attack(path='data/attack/enterprise-attack.json'):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    techniques = {}
    for o in data['objects']:
        if o.get('type') != 'attack-pattern' or o.get('revoked') or o.get('x_mitre_deprecated'):
            continue
        for ref in o.get('external_references', []):
            if ref.get('source_name') == 'mitre-attack':
                techniques[ref['external_id']] = {
                    'name': o['name'],
                    'tactics': [p['phase_name'] for p in o.get('kill_chain_phases', [])],
                    'description': o.get('description', '')[:600],
                }
    return techniques

def technique_ids_from_tags(tags):
    # attack.t1059.001 -> T1059.001
    return [t.split('attack.')[1].upper() for t in tags
            if t.startswith('attack.t') and t[8:9].isdigit()]

def load_assets(path='data/assets.yaml'):
    return yaml.safe_load(open(path, encoding='utf-8'))

FREQ = Counter()

def build_frequency(alerts):
    for a in alerts:
        FREQ[(a.rule_id or a.rule_title, a.host)] += 1

def enrich(alert, techniques, assets=None):
    assets = assets or load_assets()      # pass assets in loops: loading the file each call is slow
    ids = technique_ids_from_tags(alert.rule_tags)
    parts = []
    for t in ids:
        info = techniques.get(t)
        if info:
            tactics = ', '.join(info['tactics'])
            parts.append(t + ' ' + info['name'] + ' (tactic: ' + tactics + ')')
    attack = '; '.join(parts) or 'none mapped'
    asset = assets.get('hosts', {}).get(alert.host, assets.get('default', 'medium'))
    freq = FREQ[(alert.rule_id or alert.rule_title, alert.host)]
    return {'attack': attack, 'asset': asset, 'freq': freq, 'technique_ids': ids}
