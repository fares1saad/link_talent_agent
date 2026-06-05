from langchain.tools import tool
from googleapiclient.discovery import build
from enums.providerEnums import ProviderEnum
from config.settings import get_settings

from auth.google_auth import get_google_credentials

@tool(description="Get mail account profile information (email, total messages, threads)")
def get_mail_credentials() -> dict:

    settings = get_settings()

    if settings.provider == ProviderEnum.GOOGLE.value:

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

    if settings.provider == ProviderEnum.MICROSOFT.value:
        pass

    return profile