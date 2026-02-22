from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.embed_content(
    model="models/text-embedding-004",
    contents="What is artificial intelligence?"
)

print(response.embeddings[0].values[:10])  # print first 10 numbers