import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY,
)


if __name__ == "__main__":
    response = llm.invoke("Hi, how are you?")
    print(f"AI:\n{response.content}")