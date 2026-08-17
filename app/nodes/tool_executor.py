from app.graph.state import GraphState
from app.tools.registry import TOOLS
from app.mcp.client import call_mcp_tool
#from app.mcp.tool_executor import execute_mcp_tool
from app.mcp.utils import extract_text
from app.observability.logger import observe_node


@observe_node("tool_executor")
async def tool_executor(state: GraphState) -> GraphState:

    tool_name = state["tool_name"]

    if tool_name in TOOLS:

        result = TOOLS[tool_name](
            state["tool_input"]
        )

    # elif tool_name.startswith("mcp."):

    #     parts = tool_name.split(".")

    #     if len(parts) != 3:
    #         raise ValueError(
    #             f"Invalid MCP tool name: {tool_name}"
    #         )

    #     _, server_name, mcp_tool_name = parts

    #     result = await call_mcp_tool(
    #         server_name,
    #         mcp_tool_name,
    #         state["tool_arguments"],
    #     )

    #    

    else:

        result = await call_mcp_tool(
            tool_name,
            state["tool_arguments"],
        )

        result = extract_text(result)


    state["tool_output"] = result

    return state