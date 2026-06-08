from schemes.email import SendMailInput
from config.settings import get_settings 
from tools.templates.templateParser import TemplateParser
from auth.google_auth import get_google_credentials
from enums.mailEnums import MailEnums 
from langchain.tools import tool

@tool(
    description="""
craete an email.

if user sent the body ignore this function

For standard recruitment emails use:

email_type:
- rejection
- acceptance
- interview_invite
- missing_documents
- schedule_interview

When using one of these types, provide:
- candidate_name
- role
- company_name
and for schedule_interview also provide:
- calendar_link
and for interview_invite also provide:
- interview_date

The email body will be generated from a template automatically.

For custom emails:
- set email_type='custom'
- provide body required when email_type='custom'.

Only provide body when email_type='custom'.
"""
)
def create_email(data: SendMailInput) -> str:

    settings = get_settings()
    parser = TemplateParser(settings.language)

    if data.email_type == MailEnums.CUSTOM.value:
        return data.body

    return parser.render(
        data.email_type,
        data.model_dump()
    )



