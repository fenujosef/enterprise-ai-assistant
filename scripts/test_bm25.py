from app.retriever.bm25_retriever import BM25Retriever

retriever = BM25Retriever()

docs = retriever.retrieve(
    "VPN",
    k  = 3
)

for i, doc in enumerate(docs, start=1):
    print(f"\nResult {i}")
    print("-" * 40)

    print(doc.page_content)