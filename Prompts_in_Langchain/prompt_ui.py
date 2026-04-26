from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from langchain_core.prompts import PromptTemplate


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

template = PromptTemplate(
    template="""
    You are an expert research assistant.
    Summarize the research paper "{paper_input}" in a "{style_input}" tone.
    Keep the response "{length_input}".
    Address the user’s request: "{userinput}".
    Use clear, accurate language and avoid unrelated details.
    """,
    input_variables=["paper_input", "style_input", "length_input", "userinput"],
)

# Static prompt
user_input = st.text_input("Enter your prompt")
if st.button("Summarize"):
    prompt = template.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
            "userinput": user_input,
        }
    )
    response = model.invoke(prompt)
    print({"Response": response.content})
    st.write(response.content)
