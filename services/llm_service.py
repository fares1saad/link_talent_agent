"""LLM integration service stub."""
from typing import Any


class LLMService:
    """Simple LLM wrapper stub."""

    def __init__(self, model: str = "gpt"):
        self.model = model

    def generate(self, prompt: str, **kwargs: Any) -> str:
        """Generate text for a prompt (stub)."""
        return ""
