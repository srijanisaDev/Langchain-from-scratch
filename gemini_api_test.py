from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-2.5-flash")

print("Chat started! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chat.send_message(
        user_input,
        config={
            "max_output_tokens": 150,  # limits response size
            "temperature": 0.7         # creativity level
        }
    )

    print("AI:", response.text)
    print(response.usage_metadata)
    print()
   