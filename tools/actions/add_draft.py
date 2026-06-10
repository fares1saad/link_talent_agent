import base64
from langchain.tools import tool
from config.settings import get_settings
from providers.providerFactory import ProviderFactory

@tool(     
    description="""
    add draft email.
    this tool only add draft it does not create email body, subject or get recipient email.
    This function is used when the email body is provided by a another tool or the user.
    """
)
def add_draft(subject: str , email: str, body: str) -> bool:

    settings = get_settings()

    provider = ProviderFactory.get_provider(settings.provider)
    return provider.add_draft(
        email=email,
        body=body,
        subject=subject
    )