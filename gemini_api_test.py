from google import genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Create chat session
chat = client.chats.create(
    model="gemini-2.5-flash"
)

print("Chat started! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    response = chat.send_message(user_input)

    print("AI:", response.text)
    print()