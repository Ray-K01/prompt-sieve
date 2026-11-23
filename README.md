# llm-guard-lite

A lightweight defensive guardrail for LLM applications: detects prompt injection
(rules + LLM classifier) and scans model output for leaked secrets/PII.

> Work in progress. Authorized, defensive use only.

## Setup
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your key
python test_llm_call.py
pytest
```
