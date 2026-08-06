from app.graph.state import GraphState
from app.retriever.vector_store import get_vector_store
from app.retriever.hybrid_retriever import HybridRetriever


vector_store = get_vector_store()
retriever = HybridRetriever()

def retrieve(state: GraphState) -> GraphState:
    """Retrieve relevant document chunks."""

    docs = retriever.retrieve(
        state["rewritten_question"]
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    state["context"] = context

    return state