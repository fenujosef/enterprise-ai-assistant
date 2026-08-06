from typing import TypedDict

class GraphState(TypedDict):
    """Shared state passed between LangGraph nodes."""

    question: str
    rewritten_question: str
    context: str
    answer: str