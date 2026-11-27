from guard.output_scanner import scan_output


def test_email_detected():
    assert "email" in scan_output("Contact me at alice@example.com")


def test_clean_text_has_no_findings():
    assert scan_output("The weather is nice today") == []
