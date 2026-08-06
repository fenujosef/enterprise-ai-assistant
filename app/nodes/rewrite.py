from app.graph.state import GraphState
from app.llm.groq_client import get_llm
from app.prompts.rewrite_prompt import REWRITE_PROMPT

def rewrite(state: GraphState) -> GraphState:
    """Rewrite the user's question for better retrieval."""

    llm = get_llm()

    prompt = REWRITE_PROMPT.invoke(
        {
            "question": state["question"]
        }
    )

    response = llm.invoke(prompt)

    state["rewritten_question"] = response.content.strip()

    return state