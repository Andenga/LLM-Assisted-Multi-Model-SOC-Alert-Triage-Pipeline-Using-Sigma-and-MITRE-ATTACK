import json

from triageforge.models import TriageVerdict

with open("config/json_schema_v1.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(TriageVerdict.model_json_schema(), indent=2))

print("schema written")
