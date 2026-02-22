from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Create model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.5
)

# Invoke model
result = model.invoke("Write a 5 line poem on cricket")

print(result.content)