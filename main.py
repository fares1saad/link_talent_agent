from ipykernel import thread
from langchain.messages import HumanMessage
from dotenv import load_dotenv
from mail_agent.mail_agent import MailAgent
from config.settings import get_settings
from tools.actions.send_mail import send_mail  
from tools.actions.create_email import create_email
from tools.actions.add_draft import add_draft
from tools.inbox.search_email_criteria import search_email_criteria
from tools.inbox.read_emails import read_emails
from tools.inbox.read_threads import read_threads

load_dotenv()
settings = get_settings()


agent = MailAgent()


agent.add_tool(send_mail)
agent.add_tool(create_email)
agent.add_tool(search_email_criteria)
agent.add_tool(add_draft)
agent.add_tool(read_emails)
agent.add_tool(read_threads)

# response = agent.invoke({
#     "messages": [
#         HumanMessage(
#             content="""
# add a draft to my system for a reject canidate called Abdelrhman Adel applying for junior Talent acquisition at company MAS WELE3B with mail abdelrhmanadel1907@gmail.com 
# """
#         )
#     ]
# })

response = agent.invoke({
    "messages": [
        HumanMessage(
            content="""
i want all the emails from 7th to the 11th of june (today)
"""
        )
    ]
})
print(response['messages'][-1].content)


# - Email ID: 19ea8d1eb3b7f2b1 (thread: 19ea89ac2831e784)
# - Email ID: 19ea89c0e81ad885 (thread: 19ea89ac2831e784)
# - Email ID: 19ea89ac2831e784 (thread: 19ea89ac2831e784)