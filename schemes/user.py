"""User dataclass."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: str
    email: str
    name: Optional[str] = None
