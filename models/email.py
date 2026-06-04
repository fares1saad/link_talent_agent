"""Email dataclass."""
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Email:
    id: str
    subject: str
    body: str
    sender: str
    recipients: List[str]
    thread_id: Optional[str] = None
    timestamp: Optional[datetime] = None
