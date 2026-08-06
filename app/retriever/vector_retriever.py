from langchain_core.documents import Document

from app.retriever.base import BaseRetriever
from app.retriever.vector_store import get_vector_store

class VectorRetriever(BaseRetriever):

    def __init__(self):
        self.vector_store = get_vector_store()

    def retrieve(
        self,
        question: str,
        k: int = 3
    ) -> list[Document]:

        return self.vector_store.similarity_search(
            question,
            k=k
        )