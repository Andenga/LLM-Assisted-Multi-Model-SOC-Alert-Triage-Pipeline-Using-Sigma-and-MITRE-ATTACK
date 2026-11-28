# Hardware & Benchmark Environment

This document records the exact hardware, operating system, and runtime conditions used during TriageForge latency and throughput measurements.

## 1. Host Machine Specifications
* **CPU Model:** Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz 
* **CPU Cores / Threads:** 4 Cores / 8 Logical Processors
* **System RAM:** 15.85 GB
* **GPU Model:** Intel(R) UHD Graphics 620 (128 MB)
* **Dedicated VRAM:** N/A
* **Storage Drive (Ollama Models):** Local disk C:
* **Windows Edition & Build:**  Windows 11 Pro, Version 10.0.26300, Build 26300

## 2. Power & System State During Timing
* **Power Source:** On Battery
* **Windows Power Mode:** Balanced
* **VMware Workstation State:** VM Powered Off
* **Browser Status:** Open with multiple tabs
* **Other Active Background Apps:** VS Code, Chrome browser, Sticky notes.

## 3. Ollama Execution & Model Loading State
* **Ollama Version:** [e.g., 0.5.4]
* **Hardware Offload (`ollama ps` PROCESSOR column):**
  * `foundation-sec:8b-instruct`: 100% CPU, 5.6GB
  * `qwen3.5:9b`: 100% CPU, 6.2GB
  * `gpt-oss:20b`:  100% CPU, 13GB

