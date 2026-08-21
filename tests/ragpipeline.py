from app.retriever.hybrid_retriever import HybridRetriever
from app.retriever.reranker import Reranker
from app.llm.groq_client import get_llm


class RAGPipeline:

    def __init__(self):
        self.retriever = HybridRetriever()
        self.reranker = Reranker()
        self.llm = get_llm()

    def ask(self, question: str):

        # 1. Retrieve relevant documents
        documents = self.retriever.retrieve(question)

        # 2. Rerank retrieved documents
        reranked_documents = self.reranker.rerank(
            question,
            documents,
        )

        # 3. Build context
        context = "\n\n".join(
            document.page_content
            for document in reranked_documents
        )

        # 4. Generate answer
        prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.llm.invoke(prompt)

        # 5. Return answer
        return response.content