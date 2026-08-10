import asyncio

from app.mcp.client import call_mcp_tool


def execute_mcp_tool(
    tool_name: str,
    arguments: dict,
):
    result = asyncio.run(
        call_mcp_tool(
            tool_name,
            arguments,
        )
    )

    if not result.content:
        return ""
    
    first_content = result.content[0]

    if hasattr(first_content, "text"):
        return first_content.text

    return str(first_content)