from langchain.messages import HumanMessage
from dotenv import load_dotenv
from langchain.tools import tool
from mail_agent.mail_agent import MailAgent
from config.settings import get_settings

import os
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tools.profile import get_mail_credentials
from tools.actions.send_mail import send_mail
from tools.templates.templateParser import TemplateParser

load_dotenv()
settings = get_settings()


agent = MailAgent()


agent.add_tool(send_mail)

response = agent.invoke({
    "messages": [
        HumanMessage(
            content="""
reject canidate called Marawan Moahmed applying for junior ball controller company mas w l3b with mail marwan.m.nabil.03@gmail.com 
"""
        )
    ]
})
print(response['messages'][-1].content)


