"""Simple token store abstraction."""
from typing import Optional


class TokenStore:
    """Persist and retrieve OAuth tokens."""

    def __init__(self):
        self._store = {}

    def save(self, key: str, token: dict) -> None:
        self._store[key] = token

    def get(self, key: str) -> Optional[dict]:
        return self._store.get(key)
