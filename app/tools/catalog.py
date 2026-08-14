import asyncio

from app.tools.registry import TOOLS
from app.mcp.client import list_mcp_tools


async def get_tool_catalog() -> list[dict]:

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
    mcp_tools = await list_mcp_tools()

    for name, tool in mcp_tools.items():
        catalog.append(
            {
                "name": name,
                "source": "mcp",
                "description": tool.description or "",
                "input_schema": tool.input_schema,
            }
        )

    return catalog