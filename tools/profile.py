from langchain.tools import tool
from googleapiclient.discovery import build

from auth.google_auth import get_google_credentials

@tool
def get_gmail_credentials() -> dict:
    """
    Get Gmail account profile information (email, total messages, threads).
    """

    creds = get_google_credentials()

    service = build(
        "gmail",
        "v1",
        credentials=creds,
    )

    profile = (
        service.users()
        .getProfile(userId="me")
        .execute()
    )

    return profile