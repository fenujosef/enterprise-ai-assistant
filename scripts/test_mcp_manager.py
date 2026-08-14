import asyncio

from app.mcp.client import (
    initialize_mcp,
    list_mcp_tools,
    close_mcp,
)


async def main():

    await initialize_mcp()

    tools = await list_mcp_tools()

    print("\nDiscovered MCP Tools:\n")

    for tool in tools:
        print(f"- {tool.name}")
        print(f"  {tool.description}")

    await close_mcp()


if __name__ == "__main__":
    asyncio.run(main())