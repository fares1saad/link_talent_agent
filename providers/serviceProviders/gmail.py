
from providers.base import Provider
from auth.google_auth import get_google_credentials
from email.mime.text import MIMEText
from googleapiclient.discovery import build
import base64   


class GmailProvider(Provider):
    def send_email(self, email: str , body: str, subject: str ) -> str:

            creds = get_google_credentials()

            service = build(
                "gmail",
                "v1",
                credentials=creds,
            )

            # 3. Build MIME message
            msg = MIMEText(body)
            msg["to"] = email
            msg["subject"] = subject

            raw_message = base64.urlsafe_b64encode(
                msg.as_bytes()
            ).decode("utf-8")

            body = {"raw": raw_message}

            # 4. SEND EMAIL
            service.users().messages().send(
                userId="me",
                body=body
            ).execute()

            return True
