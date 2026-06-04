"""Gmail service skeleton."""
from typing import List, Optional
from models.email import Email


class GmailService:
    """Minimal GmailService stub."""

    def __init__(self):
        pass

    def fetch_threads(self, query: Optional[str] = None) -> List[Email]:
        """Return a list of Email objects matching a query (stub)."""
        return []

    def send_message(self, email: Email) -> None:
        """Send an email (stub)."""
        raise NotImplementedError
