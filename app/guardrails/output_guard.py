from app.guardrails.input_guard import GuardrailViolation
from app.guardrails.pii import redact_output_pii


MAX_OUTPUT_LENGTH = 8000


def validate_output(answer: str) -> str:

    if not answer:
        raise GuardrailViolation(
            "The assistant generated an empty response."
        )

    answer = answer.strip()

    if len(answer) > MAX_OUTPUT_LENGTH:
        raise GuardrailViolation(
            "The assistant response exceeds the maximum allowed length."
        )

    answer = redact_output_pii(answer)

    return answer