from abc import ABC, abstractmethod
from langchain_core.documents import Document

class BaseRetriever(ABC):
    """Abstract base class for all retrievers."""

    @abstractmethod
    def retrieve(
        self,
        question: str,
        k: int = 3
    ) -> list[Document]:
        """Retrieve relevant documents."""
        pass