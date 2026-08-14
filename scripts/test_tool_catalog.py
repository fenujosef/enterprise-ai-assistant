import asyncio

from app.mcp.client import initialize_mcp, close_mcp
from app.tools.catalog import get_tool_catalog


async def main():

    await initialize_mcp()

    try:

        catalog = await get_tool_catalog()

        print("\nTool Catalog:\n")

        for tool in catalog:

            print(f"Name: {tool['name']}")
            print(f"Source: {tool['source']}")
            print(f"Description: {tool['description']}")
            print()

    finally:

        await close_mcp()


if __name__ == "__main__":
    asyncio.run(main())