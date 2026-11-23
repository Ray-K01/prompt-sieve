# prompt-sieve

A lightweight defensive filter for LLM applications: detects prompt injection
(rules now, LLM classifier planned) and will scan model output for leaked secrets.

> Work in progress. Authorized, defensive use only.

## Setup (Windows PowerShell)
```powershell
py -m venv venv
venv\Scripts\Activate.ps1
python -m pip install pytest
python -m guard.rules
python -m pytest
```

## Setup (Linux / macOS)
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install pytest
python -m guard.rules
python -m pytest
```