from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent


load_dotenv()


class MailAgent:
    def __init__(self):
        self. tools = []
        self.agent = create_agent(
            tools=[],
             model="gpt-5-nano",
            system_prompt="You are a helpful email assistant. Use tools when needed.",
            #max_tokens=10000,


        )

    def invoke(self, input):
        return self.agent.invoke(input)
    
    def add_tool(self, tool):
        self.tools.append(tool)
        self.agent = create_agent(
            tools=self.tools,
             model="gpt-5-nano",
            system_prompt="You are a helpful email assistant. Use tools when needed.",
            #max_tokens=10000,

        )


