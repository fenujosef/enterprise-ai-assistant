from typing import TypedDict

class GraphState(TypedDict):
    """Shared state passed between LangGraph nodes."""

    question: str
    rewritten_question: str
    context: str
    answer: str
    retrieval_attempts: int
    chat_history: list[str]
    tool_name: str
    tool_input: str
    tool_output: str
    plan: list[dict]
    action: str
    current_step: int
    step_results: list[dict]