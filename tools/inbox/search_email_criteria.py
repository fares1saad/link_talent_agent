# from langchain.tools import tool
# from config.settings import get_settings
# from providers.providerFactory import ProviderFactory
# from schemes.email import SearchEmailsInput
# from utils.query_builder import build_gmail_query

# from langchain.tools import tool

# @tool(
#     args_schema=SearchEmailsInput,
#     description="""
# Search emails in the user's mailbox using one or more filters.

# Use this tool whenever the user asks to:
# -get an emails or inbox of specific day or start or end date
# - find emails from specific people,
# - retrieve unread emails,
# - search for emails containing certain subjects or keywords,
# - locate emails within a date range,
# - find emails with attachments,
# - list emails from specific folders such as Inbox or Sent.

# Do NOT use this tool to read the full contents of a specific email or an entire conversation thread.
# Use dedicated email-reading tools for those tasks.

# Examples:
# - "Show my unread emails."
# - "Find emails from Ahmed about the contract."
# - "Search for invoice emails with attachments from last month."
# - "Show emails in my inbox from the past week."

# The tool returns matching email identifiers and metadata that can be used by other tools to retrieve complete email details or thread context.
# """
# )
# def search_email_criteria(**kwargs):
#     settings = get_settings()

#     provider = ProviderFactory.get_provider(
#         settings.provider
#     )

#     filters = SearchEmailsInput.model_validate(kwargs)

#     query = build_gmail_query(filters)

#     return provider.search_emails(
#         query=query,
#         max_results=filters.max_results,
#     )



from langchain.tools import tool
from config.settings import get_settings
from providers.providerFactory import ProviderFactory
from schemes.email import SearchEmailsInput
from utils.query_builder import build_gmail_query


@tool(
    args_schema=SearchEmailsInput,
    description="""
Search emails in the user's mailbox using one or more filters.
it returns thread ID it can't Read_Threads use another tool for that.

Use this tool whenever the user asks to:
- Browse or list their inbox
- Find emails from specific people
- Retrieve unread emails
- Search for emails containing certain subjects or keywords
- Locate emails within a date range
- Find emails with attachments
- Get inbox overview for today, yesterday, this week, etc.

After calling this tool, always call read_threads with the returned thread_ids.

Examples:
- "Show my unread emails."
- "Find emails from Ahmed about the contract."
- "Search for invoice emails with attachments from last month."
- "Show emails in my inbox from the past week."
- "Get me yesterday's inbox."

Returns:
{
    "thread_ids": ["abc123", "def456"]
}
"""
)
def search_email_criteria(**kwargs) -> dict:
    settings = get_settings()
    provider = ProviderFactory.get_provider(settings.provider)

    filters = SearchEmailsInput.model_validate(kwargs)
    query = build_gmail_query(filters)

    raw_emails = provider.search_emails(
        query=query,
        max_results=filters.max_results,
    )

    if not raw_emails:
        return {"thread_ids": []}

    seen = set()
    thread_ids = []

    for email in raw_emails:
        thread_id = email.get("threadId")  # camelCase
        if thread_id and thread_id not in seen:
            seen.add(thread_id)
            thread_ids.append(thread_id)

    return {"thread_ids": thread_ids}