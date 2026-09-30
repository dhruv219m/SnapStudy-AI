# SnapStudy AI

A privacy-first, offline study assistant concept for Snapdragon-powered HP PCs.

## Current prototype
This repository contains a lightweight local retrieval prototype. It extracts text from PDFs and retrieves relevant passages using TF-IDF-style similarity. A local LLM generation layer is intentionally left as the next integration step so the project can be optimized for Snapdragon-compatible on-device inference.

## Run
```bash
pip install -r requirements.txt
python app.py notes.pdf "Explain the main concept"
```

## Snapdragon roadmap
1. Replace/augment the retrieval pipeline with a local generation model.
2. Select a compact quantized model suitable for on-device inference.
3. Evaluate Snapdragon-compatible acceleration using Qualcomm AI Hub tooling.
4. Benchmark latency, memory, power and answer quality.

## Important
This repository is a proposal/prototype scaffold. Do not claim that Snapdragon NPU deployment has been completed unless it has actually been tested.
