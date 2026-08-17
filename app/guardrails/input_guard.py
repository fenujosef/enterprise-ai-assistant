class GuardrailViolation(Exception):
    """Raised when a input violates a guardrail."""

    pass


MAX_INPUT_LENGTH = 4000


def validate_input(question: str) -> str:

    if not question:
        raise GuardrailViolation(
            "Input cannot be empty."
        )

    question = question.strip()

    if len(question) > MAX_INPUT_LENGTH:
        raise GuardrailViolation(
            "Input exceeds the maximum allowed length."
        )

    return question