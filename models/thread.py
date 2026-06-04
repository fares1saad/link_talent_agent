"""Thread dataclass."""
from dataclasses import dataclass, field
from typing import List, Optional
from .email import Email


@dataclass
class Thread:
    id: str
    subject: Optional[str] = None
    emails: List[Email] = field(default_factory=list)
