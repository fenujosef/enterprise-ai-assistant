from app.graph.state import GraphState
from app.llm.groq_client import get_llm
from app.prompts.rag_prompt import RAG_PROMPT


llm = get_llm()

def generate(state: GraphState) -> GraphState:
    """Generate the final answer."""

    prompt = RAG_PROMPT.invoke(
        {
            "history": "\n".join(state["chat_history"]),
            "question": state["question"],
            "context": state["context"]
        }
    )

    response = llm.invoke(prompt)

    state["answer"] = response.content

    state["chat_history"].append(f"User: {state['question']}")
    state["chat_history"].append(f"Assistant: {response.content}")

    return state