import base64
from email.mime.text import MIMEText
from langchain.tools import tool
from googleapiclient.discovery import build
from enums.providerEnums import ProviderEnum 
from enums.mailEnums import MailEnums
from config.settings import get_settings
from auth.google_auth import get_google_credentials
from tools.templates.templateParser import TemplateParser
from schemes.email import SendMailInput

@tool(
    description="""
Send an email.

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
- interview_link

The email body will be generated from a template automatically.

For custom emails:
- set email_type='custom'
- provide body

Only provide body when email_type='custom'.
"""
)
def send_mail(data: SendMailInput) -> bool:

    settings = get_settings()
    parser = TemplateParser(language="en")

    if data.email_type == MailEnums.REJECTION.value:
        body = parser.render(
            "reject",
            {
                "candidate_name": data.candidate_name,
                "role": data.role,
                "company_name": data.company_name
            }
        )
    elif data.email_type == MailEnums.ACCEPTANCE.value:
        body = parser.render(
            "accept",
            {
                "candidate_name": data.candidate_name,
                "role": data.role,
                "company_name": data.company_name
            }
        )
    else :
        body = data.body 


    subject = f"{data.company_name} - Application Update"

    # 2. GOOGLE PROVIDER
    if settings.provider == ProviderEnum.GOOGLE.value:

        creds = get_google_credentials()

        service = build(
            "gmail",
            "v1",
            credentials=creds,
        )

        # 3. Build MIME message
        msg = MIMEText(body)
        msg["to"] = data.email
        msg["subject"] = subject

        raw_message = base64.urlsafe_b64encode(
            msg.as_bytes()
        ).decode("utf-8")

        body = {"raw": raw_message}

        # 4. SEND EMAIL
        service.users().messages().send(
            userId="me",
            body=body
        ).execute()

        return True

    # 5. MICROSOFT (future implementation)
    if settings.provider == ProviderEnum.MICROSOFT.value:
        pass

    return False



    # print("\n" + "="*50)
    # print("REJECTION EMAIL")
    # print("="*50)
    # print(rejection_email)

    # # TODO: connect to email provider and send the message
    return False
