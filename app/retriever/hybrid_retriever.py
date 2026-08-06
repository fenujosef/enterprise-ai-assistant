from langchain_core.documents import Document
from collections import defaultdict

from app.retriever.base import BaseRetriever
from app.retriever.vector_retriever import VectorRetriever
from app.retriever.bm25_retriever import BM25Retriever


class HybridRetriever(BaseRetriever):

    def __init__(self):
        self.vector = VectorRetriever()
        self.bm25 = BM25Retriever()

    def _rff_fusion(
        self,
        vector_docs,
        bm25_docs,
        k: int = 60
    ):
        scores = defaultdict(float)
        documents = {}

        for rank, doc in enumerate(vector_docs, start=1):
            doc_id = doc.page_content
            scores[doc_id] += 1/(k + rank)
            documents[doc_id] = doc

        for rank, doc in enumerate(bm25_docs, start = 1):
            doc_id = doc.page_content
            scores[doc_id] += 1/(k + rank)
            documents[doc_id] = doc

        ranked = sorted(
            scores.items(),
            key=lambda x:x[1],
            reverse=True
        )

        return [
            documents[doc_id]
            for doc_id, _ in ranked
        ]

    def retrieve(
        self,
        question: str,
        k: int = 3
    ) -> list[Document]:
        
        vector_docs = self.vector.retrieve(question,k)

        bm25_docs = self.bm25.retrieve(question,k)

        return self._rff_fusion(
            vector_docs,
            bm25_docs
        )[:k]

        
#combined method without the rrf fusion.(Averaging similarity scores)
        """combined = vector_docs + bm25_docs

        unique_docs = []

        seen = set()

        for doc in combined:

            if doc.page_content not in seen:
                seen.add(doc.page_content)
                unique_docs.append(doc)

        return unique_docs[:k]"""