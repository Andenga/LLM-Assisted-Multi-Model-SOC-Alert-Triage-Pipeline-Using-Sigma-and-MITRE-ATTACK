# TriageForge

![CI](https://github.com/YOUR-USERNAME/triageforge/actions/workflows/ci.yml/badge.svg)
![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

TriageForge triages Windows security alerts with local LLMs (via Ollama) and measures how well they do it. It takes Sigma detections from Chainsaw, adds MITRE ATT&CK context, asks a model for a structured verdict, checks that verdict, and lets a deterministic policy make the final call. It also compares three model families on the same labeled alerts so you can see which one is safe to rely on.

It is a research prototype for decision support. It never closes or deletes an alert.

[Live sample report](https://YOUR-USERNAME.github.io/triageforge/report.html) · [Results](eval/results.md) · [Failure analysis](eval/failure_analysis.md) · [System card](docs/SYSTEM_CARD.md)

## What it does

- Turns Chainsaw/Sigma alerts into a clean, scrubbed `Alert` (no file names, hostnames or usernames reach the model).
- Enriches each alert with ATT&CK technique and tactic, asset criticality, and how often the rule fired on that host.
- Gets a schema-validated JSON verdict from a local model: verdict, confidence, technique, evidence, reasoning, actions.
- Rejects invented technique IDs and evidence that does not appear in the alert.
- Applies a safety policy: a model can lower an alert's priority in one narrow case only. High or critical rules and critical assets always escalate.
- Benchmarks three models on the same alerts, prompt and settings, and records exactly what ran (model digest, quantization, Ollama version, prompt and schema hashes, inference settings).

## How it works

```
EVTX logs → Chainsaw + Sigma → Alert → ATT&CK enrichment → scrub
          → (optional retrieval of reviewed alerts) → local LLM
          → guard (validate ID + evidence) → policy → report
```

Labels never enter the pipeline. It receives only alert IDs from the chosen split, and the test split is refused unless you pass `--final`.

## Quickstart

The demo needs no datasets and no Ollama. It runs a mock model through the full guard and policy path on sanitized sample alerts.

```powershell
git clone https://github.com/YOUR-USERNAME/triageforge.git
cd triageforge
python -m venv .venv
./.venv/Scripts/Activate.ps1
pip install -r requirements.txt
pip install -e .
python scripts/demo.py
```

With Docker (runs the mock demo only):

```powershell
docker build -t triageforge .
docker run triageforge
```

## Using real models

Install [Ollama](https://ollama.com/download), keep it on `127.0.0.1` (the default), and pull a model using the exact tag from the Ollama library:

```powershell
ollama pull qwen3.5:9b
python scripts/try_five.py local qwen3.5:9b
```

Run the pipeline on the development split:

```powershell
python -m triageforge run --provider local --model qwen3.5:9b --split dev --no-cache
```

Each run writes `results.csv` and a `config.json` manifest to `eval/results/runs/<run_id>/`.

## Models compared

| Model | Developer | Notes |
|---|---|---|
| Foundation-Sec-8B-Instruct | Cisco Foundation AI | Open-weight model built for cybersecurity (Llama 3.1 8B base) |
| qwen3.5:9b | Alibaba | General-purpose, good structured output |
| gpt-oss:20b | OpenAI | Reasoning-oriented mixture-of-experts (use `gemma4:e4b` below 16 GB RAM) |

Only one of the three was trained specifically for security. Licenses differ, so read [`docs/model_selection.md`](docs/model_selection.md) before redistributing anything.

## Results

Numbers come from `eval/results.md` only, and every figure traces to a run folder. Fill this in after your final test run:

| Test alerts | Baseline recall | Best model recall (95% CI) | Missed attacks | Queue reduction | Median s/alert |
|---|---|---|---|---|---|
| N | X% | Y% (a to b) | M | Z% | S |

These are results on a small lab dataset and one hardware setup, not a general ranking of models. If no model beats the Sigma-level baseline, that is reported as the finding.

## Security

Log text is attacker-controlled, so it is treated as untrusted input.

- The prompt wraps alerts in `<alert_data>` and tells the model never to follow instructions inside it.
- Fields are allowlisted, length-capped and stripped of invisible characters.
- 12 prompt-injection cases run per model, including a "gullible" mock model that obeys every injection. High-risk alerts still reach a human.
- A retrieval-poisoning test checks that a poisoned reference cannot suppress a high-risk alert.
- Controls are mapped to the OWASP Top 10 for LLM Applications in [`docs/threat_model.md`](docs/threat_model.md).

## Reproducibility

A lock file pins each model by digest, and `python scripts/drift_check.py` stops you from mixing results from two builds of the same tag. Run it at the start of every session. See [`docs/hardware.md`](docs/hardware.md) for the machine the timings came from.

## Project layout

```
src/triageforge/   pipeline, providers, guard, policy, retrieval, manifests
scripts/           demo, benchmarks, labeling, reports, drift check
eval/              scoring, plans, run manifests, results
prompts/           versioned system prompts (never edited after use)
config/            inference settings, model registry, JSON schema
docs/              threat model, dataset and system cards, methodology
tests/             unit and safety tests (none call a real model)
data/samples/      sanitized sample alerts for the demo
```

Raw logs, alerts and embeddings are git-ignored. Only IDs, labels and sanitized samples are committed.

## Limitations

- Lab data is cleaner than production, and sample sizes are small.
- Attack prevalence in the dataset is far higher than in a real SOC queue, so precision is also reported at 1% prevalence.
- Labels come mostly from provenance plus a reviewed sample and a second-reviewer check, not a full audit.
- Local inference is not free: electricity and hardware wear are not charged.

## Documentation

[Methodology](docs/methodology.md) · [Dataset card](docs/DATASET_CARD.md) · [Model selection](docs/model_selection.md) · [Embedding retrieval](docs/embedding_retrieval.md) · [Multi-model](docs/multi_model.md) · [Decisions](docs/decisions.md)

## Credits

[Sigma](https://github.com/SigmaHQ/sigma), [Chainsaw](https://github.com/WithSecureLabs/chainsaw), [MITRE ATT&CK](https://attack.mitre.org/), [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team), [EVTX-ATTACK-SAMPLES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES) and [Ollama](https://ollama.com/). Each dataset and model keeps its own license.

## Security policy and citation

Report vulnerabilities as described in [SECURITY.md](SECURITY.md). To cite this work, see [CITATION.cff](CITATION.cff).

## License

Code is MIT licensed. See [LICENSE](LICENSE).
