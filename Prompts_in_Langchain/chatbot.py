from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv


import os

load_dotenv()

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
model = ChatHuggingFace(llm=llm)
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = model.invoke(user_input)
    print("AI:", response)
