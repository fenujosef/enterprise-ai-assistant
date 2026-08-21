from app.guardrails.input_guard import GuardrailViolation


TOOL_POLICIES = {
    "calculator": {
        "allowed": True,
    },
    "github": {
        "allowed": True,
    },
    "slack": {
        "allowed": False,
    },
}


def authorize_tool(
    tool_name: str,
) -> None:

    policy = TOOL_POLICIES.get(
        tool_name
    )

    if policy is None:
        raise GuardrailViolation(
            f"Unknown tool: {tool_name}"
        )

    if not policy["allowed"]:
        raise GuardrailViolation(
            f"Tool '{tool_name}' is not authorized."
        )