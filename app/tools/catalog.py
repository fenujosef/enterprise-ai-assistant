import asyncio

from app.tools.registry import TOOLS
from app.mcp.client import list_mcp_tools


def get_tool_catalog() -> list[dict]:

    catalog = []

    #Local tools
    for name in TOOLS:
        catalog.append(
            {
                "name": name,
                "source": "local",
                "description": "Local application tool",
            }
        )

    #MCP tools
    mcp_tools = asyncio.run(
        list_mcp_tools()
    )

    for tool in mcp_tools:
        catalog.append(
            {
                "name": f"mcp.{tool.name}",
                "source": "mcp",
                "description": tool.description or "",
                "input_schema": tool.inputSchema,
            }
        )

    return catalog