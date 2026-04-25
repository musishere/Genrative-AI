from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
load_dotenv() 

model = ChatOpenAI(model="gpt-4.1")
response = model.invoke("What is cricket?")
print(response.content)