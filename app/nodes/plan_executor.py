from app.graph.state import GraphState
from app.tools.registry import TOOLS


def resolve_input(
    template: str,
    step_results: list[dict]
) -> str:

    resolved = template

    for result in step_results:

        placeholder = (
            f"{{step_{result['step']}_result}}"
        )

        resolved = resolved.replace(
            placeholder,
            str(result["result"])
        )

    return resolved

def plan_executor(state: GraphState) -> GraphState:

    plan = state["plan"]

    current_step = state["current_step"]

    if current_step >= len(plan["steps"]):
        return state

    step = plan["steps"][current_step]

    tool_name = step["tool"]
    tool_input = resolve_input(step["input"], state["step_results"])

    tool = TOOLS.get(tool_name)

    if tool is None:

        result = f"Tool '{tool_name}' not found."

    else:

        result = tool(tool_input)

    state["step_results"].append(
        {
            "step": step["step"],
            "action": step["action"],
            "tool": tool_name,
            "input": tool_input,
            "result": result,
        }
    )

    state["current_step"] += 1

    return state