"""Authentication helper service."""
from typing import Optional

from auth.outlook_auth import OutlookAuth
from auth.token_store import TokenStore


class AuthService:
    """Auth-related utilities/wrappers."""

    def __init__(self, provider: str = "outlook", token_store: Optional[TokenStore] = None):
        self.provider = provider.lower()
        self.token_store = token_store or TokenStore()
        self.client = None

        if self.provider == "outlook":
            self.client = OutlookAuth(token_store=self.token_store)

    def get_access_token(self) -> Optional[str]:
        """Return an access token for the selected provider or None."""
        if self.provider == "outlook" and self.client:
            return self.client.get_access_token()
        return None
