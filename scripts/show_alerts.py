from triageforge.detect import load_alerts

alerts = load_alerts('data/alerts/attack_alerts.json', origin='public_attack')
print('Loaded', len(alerts), 'alerts')
for a in alerts[:3]:
    print(a.model_dump_json(indent=2))
