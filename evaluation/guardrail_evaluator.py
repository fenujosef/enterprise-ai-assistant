import json

from app.guardrails.tool_guard import authorize_tool

from app.guardrails.input_guard import GuardrailViolation, validate_input
from app.guardrails.injection import validate_against_injection
from app.guardrails.pii import redact_input_pii
from app.guardrails.output_guard import validate_output


def evaluate_case(case):

    name = case["name"]
    text = case["input"]
    expected = case["expected_action"]

    if name == "oversized_input":
        text = "A" * 5000

    try:

        text = validate_input(text)

        text = validate_against_injection(text)

        redacted = redact_input_pii(text)

        if redacted != text:
            actual = "redact"
        else:
            actual = "allow"

    except GuardrailViolation:

        actual = "block"

    return {
        "name": name,
        "expected": expected,
        "actual": actual,
        "passed": actual == expected,
    }


def test_tool_authorization():

    allowed_tools = [
        "calculator",
        "github",
    ]

    denied_tools = [
        "slack",
        "unknown_tool",
    ]

    for tool in allowed_tools:

        try:
            authorize_tool(tool)
            print(
                f"PASS | allowed tool | {tool}"
            )

        except GuardrailViolation:

            print(
                f"FAIL | allowed tool | {tool}"
            )

    for tool in denied_tools:

        try:
            authorize_tool(tool)

            print(
                f"FAIL | denied tool executed | {tool}"
            )

        except GuardrailViolation:

            print(
                f"PASS | denied tool blocked | {tool}"
            )


def evaluate_output_case(case):

    name = case["name"]
    text = case["output"]
    expected = case["expected_action"]

    if name == "oversized_output":
        text = "A" * 9000

    try:

        result = validate_output(text)

        if result != text:
            actual = "redact"
        else:
            actual = "allow"

    except GuardrailViolation:

        actual = "block"

    return {
        "name": name,
        "expected": expected,
        "actual": actual,
        "passed": actual == expected,
    }



def main():

    with open(
        "evaluation/guardrail_dataset.json",
        "r",
        encoding="utf-8",
    ) as file:

        cases = json.load(file)

    results = []

    for case in cases:

        result = evaluate_case(case)

        results.append(result)

        status = (
            "PASS"
            if result["passed"]
            else "FAIL"
        )

        print(
            f"{status} | "
            f"{result['name']} | "
            f"expected={result['expected']} | "
            f"actual={result['actual']}"
        )

    passed = sum(
        result["passed"]
        for result in results
    )

    print("\n==============================")
    print("GUARDRAIL TEST REPORT")
    print("==============================")

    print(
        f"Passed: {passed}/{len(results)}"
    )

    print(
        f"Pass rate: "
        f"{passed / len(results):.2%}"
    )


if __name__ == "__main__":
    main()