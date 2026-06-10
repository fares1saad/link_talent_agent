from langchain.tools import tool
from config.settings import get_settings
from providers.providerFactory import ProviderFactory


@tool(
    description="""Read entire thread/conversation.
    the input is a list of thread_ID and it can be list of one thread_ID.
    Use this tool after search_email_criteria returns thread_ids to get full conversation content.

"""
)
def read_threads(thread_ids: list[str]) -> list:
    settings = get_settings()
    provider = ProviderFactory.get_provider(settings.provider)

    return [provider.read_thread(thread_id) for thread_id in thread_ids]



