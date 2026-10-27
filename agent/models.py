from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(model = 'google_genai:gemini-3.8-flash')

# response = model.invoke("tell me something about the sun in 2 sentences")
# print(response.content)