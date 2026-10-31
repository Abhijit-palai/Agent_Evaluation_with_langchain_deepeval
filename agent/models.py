from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    model="gemma-4-31b-it",
    model_provider="google_genai",
    temperature=0
)

# response = model.invoke("tell me something about the sun in 2 sentences")
# print(response.content)