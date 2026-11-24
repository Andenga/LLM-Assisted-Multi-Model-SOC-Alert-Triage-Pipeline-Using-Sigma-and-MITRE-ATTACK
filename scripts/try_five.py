import sys

from triageforge import triage
from triageforge.detect import load_alerts
from triageforge.enrich import build_frequency, enrich, load_assets, load_attack

provider = sys.argv[1] if len(sys.argv) > 1 else 'mock'
model = sys.argv[2] if len(sys.argv) > 2 else 'mock'

alerts = load_alerts('data/alerts/attack_alerts.json', origin='public_attack')
build_frequency(alerts)
techniques, assets = load_attack(), load_assets()
with open('prompts/v1_guarded.txt', encoding='utf-8') as f:
    system = f.read()
    
for a in alerts[:5]:
    info = enrich(a, techniques, assets)
    fields = '\n'.join(k + ': ' + str(v) for k, v in a.fields.items())
    ctx = ('Rule: ' + a.rule_title + ' (level: ' + a.rule_level + ')\n'
           + 'ATT&CK: ' + info['attack'] + '\nAsset criticality: ' + info['asset'] + '\n' + fields)
    user = '<alert_data>\n' + ctx + '\n</alert_data>'
    v, stats, failed, raw = triage.ask(triage.PROVIDERS[provider], system, user, model)
    print('=' * 60)
    print(ctx[:600])
    print('--> verdict:', v.verdict, v.confidence, '| failed parse:', failed,
          '| tok/s:', stats.get('generated_tokens_per_second'), '| wall s:', round(stats['sec'], 1))
    print(v.reasoning)
