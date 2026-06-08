from typing import Literal
from pydantic import BaseModel, Field


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