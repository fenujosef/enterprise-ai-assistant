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
    
    # System prompt / instruction extraction
    r"show\s+me\s+.*hidden\s+instructions",
    r"reveal\s+.*hidden\s+instructions",
    r"tell\s+me\s+.*hidden\s+instructions",
    r"show\s+.*internal\s+instructions",
    r"reveal\s+.*internal\s+instructions",

    r"what\s+are\s+your\s+system\s+instructions",
    r"what\s+are\s+your\s+hidden\s+instructions",
    r"what\s+instructions\s+were\s+you\s+given",

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