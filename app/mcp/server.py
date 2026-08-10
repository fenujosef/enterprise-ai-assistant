from mcp.server import MCPServer


mcp = MCPServer("Enterprise AI Tools")

@mcp.tool()
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        result = eval(expression)
        return str(result)

    except Exception:
        return "Invalid mathematical expression."


if __name__ == "__main__":
    mcp.run()