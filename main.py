from langchain.messages import HumanMessage
from dotenv import load_dotenv
from langchain.tools import tool
from sh_agent.mail_agent import MailAgent


import os
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tools.profile import get_gmail_credentials
load_dotenv()

agent = MailAgent()


agent.add_tool(get_gmail_credentials)

response = agent.invoke(
    {"messages": [HumanMessage(content="What is my Gmail profile?")]}
)
print(response['messages'][-1].content)
