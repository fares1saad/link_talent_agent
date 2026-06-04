"""Simple in-memory inbox memory."""
from typing import List
from models.email import Email


class InboxMemory:
    """A tiny in-memory store for emails."""

    def __init__(self):
        self._emails: List[Email] = []

    def add(self, email: Email) -> None:
        self._emails.append(email)

    def list(self) -> List[Email]:
        return list(self._emails)
