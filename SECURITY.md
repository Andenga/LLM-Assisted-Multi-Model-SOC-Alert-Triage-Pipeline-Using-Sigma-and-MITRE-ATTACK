# Security Policy

## Project Status & Disclaimer
LLM-Assisted Multi Model SOC Alert Triage Pipeline Using Sigma and MITRE ATTACK is an academic and portfolio research prototype built to evaluate local LLMs for SOC alert triage. It is **not** a production security tool and should not be deployed in live enterprise environments without independent security hardening.

## Local Execution & Data Handling
* **Local-Only Inference:** All LLM inference runs locally via Ollama bound to `127.0.0.1` (`localhost`). No alert logs or telemetry are transmitted to external cloud APIs.
* **Sensitive Artifacts:** Raw event logs (`.evtx`), local datasets, and raw model responses are excluded from version control via `.gitignore` and scanned prior to commit using Gitleaks.

## Reporting a Vulnerability
If you discover a security issue or vulnerability in this repository:
1. **Do not** open a public GitHub issue.
2. Report it privately using GitHub's **Private Vulnerability Reporting** feature (under the **Security** tab of this repo) or by contacting me directly through Linkedin at Lydia Andenga.
