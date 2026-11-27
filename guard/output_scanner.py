import re

EMAIL = re.compile(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", re.IGNORECASE)


def scan_output(text: str) -> list:
    """Return a list of leak types found in the model's reply."""
    findings = []
    if EMAIL.search(text):
        findings.append("email")
    return findings
