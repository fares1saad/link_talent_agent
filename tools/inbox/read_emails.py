from langchain.tools import tool
from config.settings import get_settings
from providers.providerFactory import ProviderFactory


@tool(
    description="""Read the content of one or more emails by ID.

Use this when the user wants to read email content. Input is a list of email IDs (pass a single ID as a one-element list).

Returns a list of dicts, each with:
{
    "id": ...,
    "thread_id": ...,
    "from": ...,
    "to": ...,
    "subject": ...,
    "date": ...,
    "snippet": ...,
    "body": ...
}
"""
)
def read_emails(email_ids: list[str]) -> list[dict]:
    settings = get_settings()
    provider = ProviderFactory.get_provider(settings.provider)

    return [provider.read_email(email_id) for email_id in email_ids]