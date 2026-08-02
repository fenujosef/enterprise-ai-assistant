from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings

from app.logging import logger
from app.settings import settings


@lru_cache
def get_embedding_model():
    """Return a singleton embedding model."""

    logger.info(f"Loading embedding model: {settings.embedding_model}")


    return HuggingFaceEmbeddings(
        model_name=settings.embedding_model
    )
