from app.graph.state import GraphState
from app.tools.registry import TOOLS
from app.mcp.tool_executor import execute_mcp_tool


def tool_executor(state: GraphState) -> GraphState:

    tool_name = state["tool_name"]

    if tool_name in TOOLS:

        result = TOOLS[tool_name](
            state["tool_input"]
        )

    elif tool_name.startswith("mcp."):

        mcp_tool_name = tool_name.removeprefix("mcp.")

        result = execute_mcp_tool(
            mcp_tool_name,
            state["tool_arguments"],
        )

    else:

        result = f"Tool '{tool_name}' not found."

    state["tool_output"] = result

    return state