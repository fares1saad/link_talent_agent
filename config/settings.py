"""Project settings (placeholders)."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Google OAuth placeholders
GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""

# Outlook / Microsoft Graph placeholders
OUTLOOK_TENANT_ID = "common"
OUTLOOK_CLIENT_ID = ""
OUTLOOK_CLIENT_SECRET = ""
OUTLOOK_REDIRECT_URI = "http://localhost:8000/getAToken"
OUTLOOK_SCOPES = [
    "Mail.ReadWrite",
    "Mail.Send",
    "offline_access",
    "User.Read",
]

# LLM settings
LLM_MODEL = "gpt"
