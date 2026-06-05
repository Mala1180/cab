import os

from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

api_key = SecretStr(os.getenv("OPENROUTER_API_KEY", ""))

model_name: str = "gemini-3.1-flash-lite-preview"

# google gemini
llm = ChatGoogleGenerativeAI(model=model_name)
