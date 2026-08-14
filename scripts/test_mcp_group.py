import asyncio

from app.mcp.client import (
    initialize_mcp,
    list_mcp_tools,
    close_mcp,
)


async def main():

    await initialize_mcp()

    try:

        tools = await list_mcp_tools()

        print("\nMCP Tools:\n")

        for name, tool in tools.items():

            print(f"Name: {name}")
            print(f"Description: {tool.description}")
            print(f"Input Schema: {tool.input_schema}")
            print()

    finally:

        await close_mcp()


if __name__ == "__main__":
    asyncio.run(main())