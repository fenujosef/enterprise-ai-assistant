import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


PROJECT_ROOT = Path(__file__).resolve().parents[2]


server_params = StdioServerParameters(
    command=sys.executable,
    args=["-m", "app.mcp.server"],
    cwd=PROJECT_ROOT,
)


async def list_mcp_tools():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.list_tools()

            return result.tools

async def get_mcp_tools():
    tools = await list_mcp_tools()
    return {
        tool.name: tool
        for tool in tools
    }


async def call_mcp_tool(
        tool_name: str,
        arguments: dict,
):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(
                tool_name,
                arguments=arguments,
            )

            return result