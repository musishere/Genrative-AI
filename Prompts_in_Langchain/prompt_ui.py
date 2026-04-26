from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from langchain_core.prompts import load_prompt


load_dotenv()
st.header("Research Tool")

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview", temperature=0.9, max_tokens=20
)

paper_input = st.selectbox("Select your paper", ["Attention is all you need"])
style_input = st.selectbox("Select input style", ["Begginer friendly", "Advanced"])
length_input = st.selectbox(
    "Select input length", ["Short 1-2 line paragraph", "Long 5-10 lines paragraph"]
)
template = load_prompt("template.json")

# Static prompt
user_input = st.text_input("Enter your prompt")
if st.button("Summarize"):
    chain = template | model
    result = chain.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
            "userinput": user_input,
        }
    )
    st.write(result.content)
