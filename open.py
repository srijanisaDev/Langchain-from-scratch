from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # loads OPENAI_API_KEY from .env [web:17]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)  # model name can be changed [web:17]

resp = llm.invoke("Write a 1-line joke about databases.")
print(resp.content)
