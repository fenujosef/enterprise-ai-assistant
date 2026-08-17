import re

from app.guardrails.input_guard import GuardrailViolation



INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"ignore\s+(all\s+)?prior\s+instructions",
    r"disregard\s+(all\s+)?previous\s+instructions",
    r"forget\s+(all\s+)?previous\s+instructions",
    r"reveal\s+(the\s+)?system\s+prompt",
    r"show\s+(me\s+)?(the\s+)?system\s+prompt",
    r"print\s+(the\s+)?system\s+prompt",
    r"reveal\s+your\s+instructions",
    r"bypass\s+(the\s+)?security",
    r"disable\s+(the\s+)?security",
]


def detect_prompt_injection(
    text: str,
) -> bool:

    normalized = text.lower().strip()

    for pattern in INJECTION_PATTERNS:

        if re.search(
            pattern,
            normalized,
        ):
            return True

    return False


def validate_against_injection(
    text: str,
) -> str:

    if detect_prompt_injection(text):

        raise GuardrailViolation(
            "Potential prompt injection detected."
        )

    return text