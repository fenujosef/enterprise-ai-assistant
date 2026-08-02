from app.logging import logger
from app.retriever.loader import load_documents
from app.retriever.splitter import split_documents
from app.retriever.vector_store import get_vector_store

def main():

    logger.info("Loading documents...")

    documents = load_documents()

    logger.info("Splitting documents...")

    chunks = split_documents(documents)

    logger.info("Creating vector store...")

    vector_store = get_vector_store()

    logger.info("Adding chunks")

    vector_store.add_documents(chunks)

    logger.info("Finished indexing documents.")


if __name__ == "__main__":
    main()