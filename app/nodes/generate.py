from app.graph.state import GraphState
from app.llm.groq_client import get_llm
from app.prompts.rag_prompt import RAG_PROMPT
from app.observability.logger import observe_node


llm = get_llm()


@observe_node("generate")
def generate(state: GraphState) -> GraphState:
    """Generate the final answer."""

    prompt = RAG_PROMPT.invoke(
        {
            "history": "\n".join(state["chat_history"]),
            "question": state["question"],
            "context": state["context"],
            "tool_output":state["tool_output"]
        }
    )

    response = llm.invoke(prompt)

    state["answer"] = response.content

    state["chat_history"].append(f"User: {state['question']}")
    state["chat_history"].append(f"Assistant: {response.content}")

    return state