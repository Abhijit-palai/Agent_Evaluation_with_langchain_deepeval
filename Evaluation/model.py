from deepeval.models import GeminiModel
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini Model via DeepEval
eval_model = GeminiModel(
    model="gemma-4-31b-it",  # or your preferred Gemini model
      # or export GOOGLE_API_KEY in your environment / .env
    temperature=0
)