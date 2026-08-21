from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    groq_api_key: str = Field(..., alias="GROQ_API_KEY")

    model_name: str = Field(
        default="openai/gpt-oss-120b",
        alias="MODEL_NAME"
    )

    embedding_model: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2",
        alias="EMBEDDING_MODEL"
    )

    chroma_db_path: str = Field(
        default="./chroma_db",
        alias="CHROMA_DB_PATH"
    )

    data_path: str = Field(
        default="./data",
        alias="DATA_PATH"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    chunk_size: int = Field(
        default=1000,
        alias="CHUNK_SIZE"
    )

    chunk_overlap: int = Field(
        default=200,
        alias="CHUNK_OVERLAP"
    )

    redis_url: str = Field(
    default="redis://redis:6379/0",
    alias="REDIS_URL"
    )

    environment: str = "development"


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()

settings = get_settings()
