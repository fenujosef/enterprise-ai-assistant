from functools import lru_cache

from langchain_groq import ChatGroq

from app.logging import logger
from app.settings import settings


@lru_cache
def get_llm() -> ChatGroq:
    """Return a singleton Groq instance."""

    logger.info(f"Loading Groq model: {settings.model_name}")

    return ChatGroq(
        model=settings.model_name,
        api_key=settings.groq_api_key,
        temperature=0
    )