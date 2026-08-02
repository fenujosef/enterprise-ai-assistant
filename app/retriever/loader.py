from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from app.logging import logger
from app.settings import settings

def load_documents():
    """Load all PDFs from the data directory."""

    documents = []

    data_path = Path(settings.data_path)

    pdf_files = list(data_path.glob("*.pdf"))

    logger.info(f"Found {len(pdf_files)} PDF(s).")

    for pdf in pdf_files:
        logger.info(f"Loading {pdf.name}")

        loader = PyPDFLoader(str(pdf))

        documents.extend(loader.load())

    logger.info(f"Loaded {len(documents)} pages.")

    return documents    