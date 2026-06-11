from typing import Literal
from pydantic import BaseModel, Field
from typing import Optional


from typing import Literal
from pydantic import BaseModel, Field
from typing import Optional


class SendMailInput(BaseModel):
    email_type: Literal[
        "rejection",
        "missing_documents",
        "intent_to_offer",
        "offer_follow_up",
        "formal_offer_onboarding",
        "post_interview_feedback",
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

    body: str | None = Field(
        default=None,
        description="Required only when email_type='custom'."
    )

    recruiter_name: str | None = Field(
        default=None,
        description="Name of recruiter sending the email."
    )

    job_title: str | None = Field(
        default=None,
        description="Job title (used across offer, rejection, feedback emails)."
    )

    expected_start_date: str | None = Field(
        default=None,
        description="Candidate expected start date (intent_to_offer)."
    )

    current_address: str | None = Field(
        default=None,
        description="Candidate residential address (intent_to_offer)."
    )

    planned_holidays: str | None = Field(
        default=None,
        description="Planned holidays in next 3-6 months (intent_to_offer)."
    )

    salary: str | None = Field(
        default=None,
        description="Base salary amount (formal_offer_onboarding)."
    )

    currency: str | None = Field(
        default=None,
        description="Salary currency (e.g. USD, EUR, EGP)."
    )

    start_date: str | None = Field(
        default=None,
        description="Official start date (formal_offer_onboarding)."
    )

    work_location: str | None = Field(
        default=None,
        description="Work location (formal_offer_onboarding)."
    )

    manager_name: str | None = Field(
        default=None,
        description="Reporting manager name (formal_offer_onboarding)."
    )

    deadline_date: str | None = Field(
        default=None,
        description="Deadline to sign and return offer (formal_offer_onboarding)."
    )

    missing_items: str | None = Field(
        default=None,
        description="List of missing documents (missing_documents)."
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
        description="Only emails after this date. Format: YYYY/MM/DD or since 2024/01/01 or 7d ago"
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