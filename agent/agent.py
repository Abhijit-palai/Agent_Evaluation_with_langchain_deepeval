from models import model
from tools import calculate_right_refund , get_today_date , issue_refund_ticket , get_user_purchase_history
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from prompts import agent_system_prompt
from objects import Answer
from langgraph.checkpoint import InMemorySaver
from langchain.messages import HumanMessage
from uuid import uuid4

agent = create_agent(
    model = model,
    system_prompt = agent_system_prompt,
    tools = [calculate_right_refund , get_user_purchase_history , get_today_date , issue_refund_ticket],
    response_format = Answer,
    checkpointer=InMemorySaver()
)