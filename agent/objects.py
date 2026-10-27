from pydantic import BaseModel , Field 

class Answer(BaseModel):
    answer:str = Field(description = "the answer that is needed fir the user question" )
    conversation:bool = Field(description = "This is an indicator to know if the conversation should still continue or not. if the agent has made the decision about the refund this should be False . if the conversation still need more talk then it's true" , default=True)
    
class PurchaseItem(BaseModel):
    name:str = Field(description = "name of the item purchased")
    