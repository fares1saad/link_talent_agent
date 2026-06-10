from providers.base import Provider
from auth.google_auth import get_google_credentials
from email.mime.text import MIMEText
from googleapiclient.discovery import build
import base64  
import re 


class GmailProvider(Provider):

    def __init__(self):
        super().__init__()
        self.creds = get_google_credentials()
        self.service = build(
            "gmail",
            "v1",   
            credentials=self.creds,
        )
         
    def send_email(self, email: str, body: str, subject: str) -> str:
        msg = MIMEText(body)
        msg["to"] = email
        msg["subject"] = subject

        raw_message = base64.urlsafe_b64encode(
            msg.as_bytes()
        ).decode("utf-8")

        self.service.users().messages().send(
            userId="me",
            body={"raw": raw_message}
        ).execute()

        return True
    
    def add_draft(self, email: str, body: str, subject: str) -> bool:
        msg = MIMEText(body)
        msg["to"] = email
        msg["subject"] = subject

        raw_message = base64.urlsafe_b64encode(
            msg.as_bytes()
        ).decode("utf-8")

        self.service.users().drafts().create(
            userId="me",
            body={"message": {"raw": raw_message}}
        ).execute()

        return True
    
    def search_emails(self, query: str, max_results: int = 20):
        results = (
            self.service.users()
            .messages()
            .list(
                userId="me",
                q=query,
                maxResults=max_results
            )
            .execute()
        )
        return results.get("messages", [])

    def read_email(self, email_id: str) -> dict:
        msg = (
            self.service.users()
            .messages()
            .get(
                userId="me",
                id=email_id,
                format="full"
            )
            .execute()
        )

        payload = msg.get("payload", {})
        headers = {
            h["name"]: h["value"]
            for h in payload.get("headers", [])
        }

        return {
            "id": msg.get("id"),
            "thread_id": msg.get("threadId"),
            "from": headers.get("From"),
            "to": headers.get("To"),
            "subject": headers.get("Subject"),
            "date": headers.get("Date"),
            #"snippet": msg.get("snippet"),
            "body": self._strip_quotes(self._extract_body(payload)),
        }

    def read_thread(self, thread_id: str) -> dict:
        thread = (
            self.service.users()
            .threads()
            .get(
                userId="me",
                id=thread_id,
                format="full"
            )
            .execute()
        )

        messages = thread.get("messages", [])
        parsed_messages = []

        for msg in messages:
            payload = msg.get("payload", {})
            headers = {
                h["name"]: h["value"]
                for h in payload.get("headers", [])
            }

            parsed_messages.append({
                "id": msg.get("id"),
                "thread_id": msg.get("threadId"),
                "from": headers.get("From"),
                "to": headers.get("To"),
                "subject": headers.get("Subject"),
                "date": headers.get("Date"),
                #"snippet": msg.get("snippet"),
                "body": self._strip_quotes(self._extract_body(payload)),
            })

        return {
            "thread_id": thread_id,
            "messages": parsed_messages
        }

    def _extract_body(self, payload: dict) -> str:
        if not payload:
            return ""

        if "parts" in payload:
            for part in payload["parts"]:
                if part.get("mimeType") == "text/plain":
                    data = part.get("body", {}).get("data")
                    if data:
                        return base64.urlsafe_b64decode(
                            data
                        ).decode("utf-8", errors="ignore")

            for part in payload["parts"]:
                if part.get("mimeType") == "text/html":
                    data = part.get("body", {}).get("data")
                    if data:
                        return base64.urlsafe_b64decode(
                            data
                        ).decode("utf-8", errors="ignore")

        data = payload.get("body", {}).get("data")
        if data:
            return base64.urlsafe_b64decode(
                data
            ).decode("utf-8", errors="ignore")

        return ""

    def _strip_quotes(self, body: str) -> str:
        lines = body.splitlines()
        clean = []
        for line in lines:
            if line.strip().startswith("On ") and line.strip().endswith("wrote:"):
                break
            if line.startswith(">"):
                continue
            clean.append(line)
        return "\n".join(clean).strip()