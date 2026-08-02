from functools import lru_cache

from langchain_chroma import Chroma

from app.embeddings.embedding_model import get_embedding_model
from app.logging import logger
from app.settings import settings


@lru_cache
def get_vector_store():
    """Return a persistent ChromaDB instance."""

    logger.info(f"Initializing ChromaDB...")

    return Chroma(
        persist_directory=settings.chroma_db_path,
        embedding_function=get_embedding_model()
    )