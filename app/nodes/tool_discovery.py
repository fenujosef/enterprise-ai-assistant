from app.graph.state import GraphState
from app.tools.catalog import get_tool_catalog


def tool_discovery(state: GraphState) -> GraphState:

    state["tool_catalog"] = get_tool_catalog()

    return state