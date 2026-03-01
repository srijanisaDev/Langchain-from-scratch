from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()



model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
)


class Review(TypedDict):
    summary : str
    sentiment: str


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" The hardware is great , but the software feels bloated . There are too many pre installed apps 
                                 also , the ui looks outdated compared to other brands . Hoping for a softwaare update to fix this .



""")
    

print(result)
print(result['summary'])
print(result['sentiment'])    