from guard.output_scanner import scan_output


def test_email_detected():
    assert "email" in scan_output("Contact me at alice@example.com")


def test_clean_text_has_no_findings():
    assert scan_output("The weather is nice today") == []


def test_api_key_detected():
    assert "api_key" in scan_output(
        "Here is the key: sk-abcdefghijklmnopqrstuvwxyz")


def test_normal_sentence_not_flagged_as_key():
    assert "api_key" not in scan_output("I like skiing")


def test_word_ending_in_sk_not_flagged_as_key():
    assert "api_key" not in scan_output(
        "Run the disk-partitionmanagementutility tool")
