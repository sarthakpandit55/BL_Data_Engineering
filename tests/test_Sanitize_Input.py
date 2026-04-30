import pytest

import source.Sanitize_Input as SI

def test_name():
    text = "Sarthak@$#"
    assert SI.sanitize_input(text) == "Sarthak"


def test_payment():
    text = "Payment: 100$"
    assert SI.sanitize_input(text) == "Payment 100"

def test_text():
    text = "!@#$%"
    with pytest.raises(SI.InputSanitizeError, match = "Empty input, please enter text"):
        SI.sanitize_input(text)
