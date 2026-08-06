from app.retriever.hybrid_retriever import HybridRetriever
from app.retriever.reranker import Reranker

retriever = HybridRetriever()
reranker = Reranker()

docs = retriever.retrieve(
    "How many annual leave days do employees receive?",
    k=10
)

reranked = reranker.rerank(
    "How many annual leave days do employees receive?",
    docs,
    top_k=3
)

for i, doc in enumerate(reranked, start=1):
    print(f"\nResult {i}")
    print("-" * 40)
    print(doc.page_content[:300])