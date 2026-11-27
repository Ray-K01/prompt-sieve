import re

EMAIL = re.compile(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", re.IGNORECASE)
API_KEY = re.compile(r"\bsk-[A-Za-z0-9]{20,}")


def scan_output(text: str) -> list:
    """Return a list of leak types found in the model's reply."""
    findings = []
    if EMAIL.search(text):
        findings.append("email")
    if API_KEY.search(text):
        findings.append("api_key")
    return findings
