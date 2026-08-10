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
    tool_arguments: dict
    tool_output: str
    tool_catalog: list[dict]
    plan: list[dict]
    action: str
    current_step: int
    step_results: list[dict]
    reflection: str
    reflection_action: str
    retry_count: int
    
    