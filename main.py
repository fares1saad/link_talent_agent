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
from tools.intelligence.get_time_stamp import get_current_time

load_dotenv()
settings = get_settings()


agent = MailAgent()


agent.add_tool(send_mail)
agent.add_tool(create_email)
agent.add_tool(search_email_criteria)
agent.add_tool(add_draft)
agent.add_tool(read_emails)
agent.add_tool(read_threads)
agent.add_tool(get_current_time)



response = agent.invoke({
    "messages": [
        HumanMessage(
            content="""
 summarize my inbox for yesterday    
    """
        )
    ]
})
print(response['messages'][-1].content)
