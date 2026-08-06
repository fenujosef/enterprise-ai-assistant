from app.retriever.hybrid_retriever import HybridRetriever
from app.retriever.reranker import Reranker
from app.llm.groq_client import get_llm

class RAGPipeline:

    def __init__(self):
        self.retriever = HybridRetriever()
        self.reranker = Reranker()
        self.llm = get_llm()

    def ask(self, question: str):
        ...