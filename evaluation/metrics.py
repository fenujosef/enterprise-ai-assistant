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


def keyword_coverage(
    keywords: list[str],
    text: str,
) -> float:

    if not keywords:
        return 1.0

    normalized_text = normalize(text)
    matched = 0

    for keyword in keywords:
        if normalize(keyword) in normalized_text:
            matched += 1

    return round(
        matched / len(keywords),
        3,
    )


def action_match(
    expected: str | None,
    actual: str | None,
) -> bool:

    if expected is None:
        return True

    return expected == actual