"""Outlook / Microsoft Graph service."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

import requests
from auth.outlook_auth import OutlookAuth
from schemes.email import Email

GRAPH_BASE_URL = "https://graph.microsoft.com/v1.0"


class OutlookService:
    """Outlook service wrapper for Microsoft Graph email operations."""

    def __init__(self, auth_client: Optional[OutlookAuth] = None):
        self.auth_client = auth_client or OutlookAuth()

    def _headers(self) -> Dict[str, str]:
        access_token = self.auth_client.get_access_token()
        if not access_token:
            raise RuntimeError("Outlook access token is not available.")
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def fetch_messages(self, folder: Optional[str] = None, query: Optional[str] = None) -> List[Email]:
        path = folder or "Inbox"
        url = f"{GRAPH_BASE_URL}/me/mailFolders/{path}/messages"
        params: Dict[str, Any] = {
            "$top": 25,
            "$select": "id,subject,bodyPreview,from,toRecipients,conversationId,receivedDateTime",
        }
        if query:
            params["$filter"] = f"contains(subject,'{query}')"
        response = requests.get(url, headers=self._headers(), params=params)
        response.raise_for_status()
        items = response.json().get("value", [])
        return [self._message_to_email(item) for item in items]

    def send_message(self, email: Email) -> None:
        payload = {
            "message": {
                "subject": email.subject,
                "body": {"contentType": "Text", "content": email.body},
                "toRecipients": [
                    {"emailAddress": {"address": recipient}} for recipient in email.recipients
                ],
            },
            "saveToSentItems": True,
        }
        response = requests.post(
            f"{GRAPH_BASE_URL}/me/sendMail",
            headers=self._headers(),
            json=payload,
        )
        response.raise_for_status()

    @staticmethod
    def _message_to_email(item: Dict[str, Any]) -> Email:
        sender = item.get("from", {}).get("emailAddress", {}).get("address", "")
        recipients = [
            recipient.get("emailAddress", {}).get("address", "")
            for recipient in item.get("toRecipients", [])
        ]
        return Email(
            id=item.get("id", ""),
            subject=item.get("subject", ""),
            body=item.get("bodyPreview", ""),
            sender=sender,
            recipients=recipients,
            thread_id=item.get("conversationId"),
            timestamp=item.get("receivedDateTime"),
        )
