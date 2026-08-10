import asyncio

from app.mcp.client import list_mcp_tools
from app.mcp.client import call_mcp_tool


async def main():

    # tools = await list_mcp_tools()

    # print("\nMCP Tools:\n")

    # for tool in tools:
    #     print(f"Name: {tool.name}")
    #     print(f"Description: {tool.description}")
    #     print(f"Schema: {tool.input_schema}")
    #     print()


    result = await call_mcp_tool(
            "calculator",
            {
                "expression": "25 * 18"
            }
        )

    print("\nMCP Tool Result:\n")

    for content in result.content:
            print(content)


if __name__ == "__main__":
    asyncio.run(main())