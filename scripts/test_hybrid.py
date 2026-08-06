from app.retriever.hybrid_retriever import HybridRetriever

retriever = HybridRetriever()

docs = retriever.retrieve(
    "annual leave",
    k=3
)

for i, doc in enumerate(docs, start=1):
    print(f"\nResult {i}")
    print("-" * 40)
    print(doc.page_content)