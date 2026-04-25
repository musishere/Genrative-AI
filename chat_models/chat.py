from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv() 

# model = ChatOpenAI(model="gpt-4.1")
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=0.9,max_tokens=20)
response = model.invoke("write a poem on AI")
print(response.content)