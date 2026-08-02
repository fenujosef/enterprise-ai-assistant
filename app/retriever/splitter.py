from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.logging import logger
from app.settings import settings

def split_documents(documents):
    """Split documents into overlapping chunks."""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = settings.chunk_size,
        chunk_overlap = settings.chunk_overlap
    )

    chunks = splitter.split_documents(documents)

    logger.info(f"Created {len(chunks)} chunks.")

    return chunks