import re

def normalize(text: str) -> str:

    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)

    return text


def exact_match(
        expected: str,
        actual: str,
) -> bool:

    return normalize(expected) == normalize(actual)


def contains_expected(
        expected: str,
        actual: str,
) -> bool:
    return normalize(expected) in normalize(actual)