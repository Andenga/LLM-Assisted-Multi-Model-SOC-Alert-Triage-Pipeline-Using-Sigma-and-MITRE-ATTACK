import pandas as pd
from pathlib import Path

df = pd.read_json("data/alerts/all_alerts.jsonl", lines=True)
tmap = pd.read_csv("data/attack_file_map.csv").set_index("source_file")["true_technique"]

df["file"] = df["source_file"].map(lambda p: Path(p).name)
df["true_technique"] = df["file"].map(tmap)
df["label"] = df["origin"].map({"public_attack": "true_positive",
                                "lab_benign": "false_positive"})
df["label_source"] = "dataset_origin"
df.loc[df.origin == "lab_benign", "true_technique"] = None
df["notes"] = ""

# Grouping column used for the split (see 8.5)
ts = pd.to_datetime(df["timestamp"], utc=True)
df["group"] = df["file"].where(df.origin == "public_attack",
                               df["origin"] + "_" + ts.dt.strftime("%Y%m%d_%H"))

df.to_pickle("data/alerts/labels_draft.pkl")   # git-ignored
print(df.label.value_counts(dropna=False))