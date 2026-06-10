from typing import Literal
from pydantic import BaseModel, Field
from typing import Optional


class SendMailInput(BaseModel):
    email_type: Literal[
        "rejection",
        "acceptance",
        "interview_invite",
        "missing_documents",
        "schedule_interview",
        "custom",
    ] = Field(
        description="Type of recruitment email."
    )

    subject: str = Field(
        description="Email subject line."
    )

    email: str = Field(
        description="Recipient email address."
    )

    candidate_name: str | None = Field(
        default=None,
        description="Candidate name."
    )

    role: str | None = Field(
        default=None,
        description="Job role."
    )

    company_name: str | None = Field(
        default=None,
        description="Company name."
    )

    interview_date: str | None = Field(
        default=None,
        description=(
            "Required only for interview_invite. "
            "Example: 'June 20, 2026 at 3:00 PM UTC'."
        )
    )

    interview_link: str | None = Field(
        default=None,
        description=(
            "Required only for interview_invite. "
            "Meeting URL (Google Meet, Zoom, Teams, etc)."
        )
    )

    calendar_link: str | None = Field(
        default=None,
        description=(
            "Required only for schedule_interview. "
            "Link where the candidate can choose a time slot."
        )
    )

    body: str | None = Field(
        default=None,
        description="Required only when email_type='custom'."
    )


class SearchEmailsInput(BaseModel):
    sender: Optional[str] = Field(
        default=None,
        description="Filter emails by sender email."
    )
    recipient: Optional[str] = Field(
        default=None,
        description="Filter emails by recipient email or name."
    )
    subject: Optional[str] = Field(
        default=None,
        description="Filter emails by subject."
    )
    keywords: Optional[str] = Field(
        default=None,
        description="Words or phrases or name that should appear in the email."
    )
    start_date: Optional[str] = Field(
        default=None,
        description="Only emails after this date. Format: YYYY/MM/DD"
    )
    end_date: Optional[str] = Field(
        default=None,
        description="Only emails before this date. Format: YYYY/MM/DD"
    )
    unread_only: bool = Field(
        default=False,
        description="Only unread emails."
    )
    has_attachment: bool = Field(
        default=False,
        description="Only emails with attachments."
    )
    label: Optional[str] = Field(
        default="INBOX",
        description="Gmail label such as INBOX, SENT, DRAFT, SPAM, TRASH. Defaults to INBOX."
    )
    max_results: int = Field(
        default=20,
        description="Maximum number of emails to return."
    )