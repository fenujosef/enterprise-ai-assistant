from app.graph.state import GraphState
from app.tools.registry import TOOLS


def tool_executor(state: GraphState) -> GraphState:
    """Execute the selected tool."""

    tool_name = state["tool_name"]

    if not tool_name:
        state["tool_output"] = ""
        return state
    
    tool = TOOLS.get(tool_name)

    if tool is None:
        state["tool_output"] = "Tool not found."
        return state

    result = tool(state["tool_input"])

    state["tool_output"] = result

    return state