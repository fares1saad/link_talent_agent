from langchain.messages import HumanMessage
from dotenv import load_dotenv
from langchain.tools import tool
from mail_agent.mail_agent import MailAgent
from config.settings import get_settings
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tools.actions.send_mail import send_mail  
from tools.actions.create_email import create_email

load_dotenv()
settings = get_settings()


agent = MailAgent()


agent.add_tool(send_mail)
agent.add_tool(create_email)

response = agent.invoke({
    "messages": [
        HumanMessage(
            content="""
send a reject canidate called Abdelrhman Adel applying for junior Talent acquisition at company MAS WELE3B with mail abdelrhmanadel1907@gmail.com 
"""
        )
    ]
})
print(response['messages'][-1].content)


