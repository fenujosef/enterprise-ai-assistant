import sys
from pathlib import Path

from mcp import StdioServerParameters


PROJECT_ROOT = Path(__file__).resolve().parents[2]


MCP_SERVERS = {
    "enterprise": StdioServerParameters(
        command=sys.executable,
        args=["-m", "app.mcp.server"],
        cwd=PROJECT_ROOT,
    ),
}

