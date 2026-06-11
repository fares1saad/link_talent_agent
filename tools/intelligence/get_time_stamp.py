from datetime import datetime
from langchain_core.tools import tool


@tool
def get_current_time() -> str:
    """
    Returns the current local date and time from the machine running the agent.

    IMPORTANT: Always use this tool as the reference point when the user
    mentions relative time expressions such as "today", "yesterday",
    "tomorrow", "last week", "next Monday", "this month", "two days ago",
    or any other date or time that depends on the current moment.

    Use this tool for scheduling, deadline checks, timestamping, and any
    task that requires knowledge of the current date or time.

    Returns:
        The current local date and time as a string in the format
        YYYY-MM-DD HH:MM:SS.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")