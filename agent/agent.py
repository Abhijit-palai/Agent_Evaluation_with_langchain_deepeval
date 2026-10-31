from models import model
from tools import calculate_right_refund , get_today_date , issue_refund_ticket , get_user_purchase_history
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from prompts import agent_system_prompt
from objects import Answer
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from uuid import uuid4

agent = create_agent(
    model = model,
    system_prompt = agent_system_prompt,
    tools = [calculate_right_refund , get_user_purchase_history , get_today_date , issue_refund_ticket],
    response_format = Answer,
    checkpointer=InMemorySaver()
)

def run_conversation():
    config = {"configurable":{"thread_id":str(uuid4())}}
    
    question = HumanMessage(content = "I would like to request a refund")
    conversation = True
    
    while conversation:
        response = agent.invoke({"messages":question} , config=config)
        structure_response = response["structured_response"]
        
        print(structure_response.answer)
        
        conversation = structure_response.conversation
        
        if conversation:
            user_input = input("reply: \n")
            question = HumanMessage(content = user_input)
            
    print("Yah Finally Done. ")
    
#run_conversation()


        