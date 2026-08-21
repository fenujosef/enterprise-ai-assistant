import hashlib


def create_cache_key(
    question: str,
) -> str:

    normalized = question.strip().lower()

    digest = hashlib.sha256(
        normalized.encode("utf-8")
    ).hexdigest()

    return f"chat:v1:{digest}"