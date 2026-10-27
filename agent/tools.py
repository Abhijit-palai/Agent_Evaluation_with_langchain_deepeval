from langchain.tools import tool
from data import users_data
from dotenv import load_dotenv
import logging

from objects import PurchaseItem
from datetime import date

load_dotenv()

@tool
def get_user_purchase_history(user:str) -> dict :
    """This tool takes the user username and return a dict of the user purchase history if the user exists"""
    logging.info(f"using get_user_purchase_history tool on user: {user}")
    
    if users_data.get(user):
        return users_data[user]
    return {"status":"there was no username found."}

@tool
def calculate_right_refund(user:str , items:list[PurchaseItem])-> str:
    """this tool takes a list of items to be returned and the username and will return how much the return is worth"""
    logging.info(f"using calculate_right_refund tool to get user's ")