# SnapStudy AI

Private, local-first AI study assistant prototype for Snapdragon-powered HP PCs.

## Features
- Local PDF text extraction
- Local TF-IDF retrieval
- Relevant source passages for questions
- Streamlit interface
- No cloud API required for the core prototype
- Roadmap for local LLM and Snapdragon/NPU optimization

## Run
pip install -r requirements.txt
streamlit run app.py

## Important
The current prototype has not been represented as already deployed on Snapdragon/NPU hardware. Hardware optimization is the next development stage and must be validated on compatible hardware.

## Architecture
PDF -> local extraction -> chunking -> TF-IDF retrieval -> relevant passages -> optional local LLM -> grounded answer
