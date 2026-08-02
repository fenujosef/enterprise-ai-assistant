from app.settings import settings

"""print(settings.model_name)
print(settings.embedding_model)
print(settings.data_path)"""


from app.logging import logger

"""logger.debug("Debug message")

logger.info("Application started")

logger.warning("Low disk space")

logger.error("Unable to connect")

logger.critical("Application shutting down")"""


from app.retriever.loader import load_documents

"""documents = load_documents()

print(f"Loaded {len(documents)} pages.")

print()

print(documents[0].page_content[:500])

print()

print(documents[0].metadata)"""


from app.retriever.loader import load_documents
from app.retriever.splitter import split_documents

"""documents = load_documents()

chunks = split_documents(documents)

print(f"Pages: {len(documents)}")
print(f"Chunks: {len(chunks)}")

print("\nFirst chunk:\n")
print(chunks[0].page_content)

print("\nMetadata:\n")
print(chunks[0].metadata)"""


from app.embeddings.embedding_model import get_embedding_model

"""embedding_model = get_embedding_model()

vector = embedding_model.embed_query(
    "Employees receive annual leave."
)

print(f"Vector Dimension: {len(vector)}")

print(vector[:10])"""


from app.retriever.vector_store import get_vector_store

vector_store = get_vector_store()

results = vector_store.similarity_search(
    "How many annual leave days do employees receive?",
    k=3
)

for index, document in enumerate(results, start=1):

    print(f"\nResult {index}")

    print("-" * 40)

    print(document.page_content)

    print(document.metadata)