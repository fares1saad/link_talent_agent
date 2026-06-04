"""Vector store stub for embeddings/search."""
from typing import List, Any


class VectorStore:
    """Simple vector store stub."""

    def __init__(self):
        self._vectors: List[Any] = []

    def add(self, vector: Any) -> None:
        self._vectors.append(vector)

    def search(self, query_vector: Any, top_k: int = 5) -> List[Any]:
        return []
