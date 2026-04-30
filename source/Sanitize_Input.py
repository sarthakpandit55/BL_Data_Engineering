import re

class InputSanitizeError(Exception):
    pass

def sanitize_input(text):
    cleaned_text = re.sub(r"[^A-Za-z0-9\s-]", "", text)

    cleaned_text = cleaned_text.strip()

    if cleaned_text == "":
        raise InputSanitizeError("Empty input, please enter text")

    else:
        return cleaned_text