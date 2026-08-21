from app.guardrails.pii import redact_pii


text = """
My name is John Smith.
My email is john.smith@example.com.
My phone number is 9876543210.
"""

result = redact_pii(text)

print(result)


from app.guardrails.output_guard import validate_output


answer = """
The employee's email is john@example.com.
"""

print(validate_output(answer))


answer = "A" * 9000

validate_output(answer)