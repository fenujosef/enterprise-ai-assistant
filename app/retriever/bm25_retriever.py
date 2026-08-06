from rank_bm25 import BM25Okapi
from langchain_core.documents import Document

from app.retriever.base import BaseRetriever
from app.retriever.loader import load_documents
from app.retriever.splitter import split_documents


class BM25Retriever(BaseRetriever):

    def __init__(self):
        documents = load_documents()
        chunks = split_documents(documents)

        self.documents = chunks

        tokenized_corpus = [
            doc.page_content.split()
            for doc in chunks
        ]

        self.bm25 = BM25Okapi(tokenized_corpus)


    def retrieve(
        self,
        question: str,
        k: int = 3
    ) -> list[Document]:

        tokenized_query = question.split()
        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            zip(scores, self.documents),
            key=lambda x: x[0],
            reverse=True
        )

        return [
            doc
            for _, doc in ranked[:k]
        ]