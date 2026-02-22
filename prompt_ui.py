from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""
You are an AI research assistant.

Explain the research paper '{paper_input}' in a {style_input} style.

Explanation length: {length_input}.

Provide a clear and structured explanation.
"""
)

chain = template | model


# ✅ ADD CACHE FUNCTION HERE
@st.cache_data
def get_response(paper, style, length):
    return chain.invoke({
        "paper_input": paper,
        "style_input": style,
        "length_input": length
    })


if st.button('Summarize'):

    result = get_response(paper_input, style_input, length_input)

    st.write(result.content)