from app.graph.state import GraphState
from app.retriever.vector_store import get_vector_store
from app.retriever.hybrid_retriever import HybridRetriever
from app.retriever.reranker import Reranker


vector_store = get_vector_store()
retriever = HybridRetriever()
reranker = Reranker()

def retrieve(state: GraphState) -> GraphState:
    """Retrieve relevant document chunks."""

    docs = retriever.retrieve(
        state["rewritten_question"],
        k=10
    )

    docs = reranker.rerank(
        state["rewritten_question"],
        docs,
        top_k = 3
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    state["context"] = context

    return state