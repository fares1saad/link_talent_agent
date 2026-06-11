from schemes.email import SearchEmailsInput
from datetime import datetime
from config.settings import get_settings
import pytz


def build_gmail_query(filters: SearchEmailsInput) -> str:
    query_parts = []

    # Explicitly exclude promotions, social, updates, forums
    query_parts.append("-category:promotions")
    query_parts.append("-category:social")
    query_parts.append("-category:updates")
    query_parts.append("-category:forums")

    # Label/folder — INBOX is the default
    if filters.label and filters.label.upper() != "INBOX":
        query_parts.append(f"in:{filters.label.lower()}")
    else:
        query_parts.append("in:inbox")

    if filters.sender:
        query_parts.append(f"from:{filters.sender}")
    if filters.recipient:
        query_parts.append(f"to:{filters.recipient}")
    if filters.subject:
        query_parts.append(f'subject:"{filters.subject}"')
    if filters.keywords:
        query_parts.append(filters.keywords)
    if filters.start_date:
        unix_ts = _date_to_unix(filters.start_date)
        query_parts.append(f"after:{unix_ts}")
    if filters.end_date:
        unix_ts = _date_to_unix(filters.end_date, end_of_day=True)
        query_parts.append(f"before:{unix_ts}")
    if filters.unread_only:
        query_parts.append("is:unread")
    if filters.has_attachment:
        query_parts.append("has:attachment")

    return " ".join(query_parts)


def _date_to_unix(date_str: str, end_of_day: bool = False) -> int:
    """
    Convert YYYY/MM/DD to Unix timestamp using timezone from settings.
    end_of_day=True returns 23:59:59 of that day instead of 00:00:00.
    """
    settings = get_settings()
    tz = pytz.timezone(settings.timezone)

    date = datetime.strptime(date_str, "%Y/%m/%d")

    if end_of_day:
        date = date.replace(hour=23, minute=59, second=59)
    else:
        date = date.replace(hour=0, minute=0, second=0)

    return int(tz.localize(date).timestamp())