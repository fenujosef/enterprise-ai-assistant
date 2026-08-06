from functools import lru_cache

from sentence_transformers import CrossEncoder
from langchain_core.documents import Document


@lru_cache
def get_reranker():
    """Load the Cross Encoder once."""

    return CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L-6-v2"
    )


class Reranker:

    def __init__(self):
        self.model = get_reranker()

    def rerank(
        self,
        question: str,
        documents: list[Document],
        top_k: int = 3
    ) -> list[Document]:

        pairs = [
            (question, doc.page_content)
            for doc in documents
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(scores, documents),
            key=lambda x: x[0],
            reverse=True
        )

        return [
            doc
            for _, doc in ranked[:top_k]
        ]