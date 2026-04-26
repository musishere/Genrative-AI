from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
model = ChatHuggingFace(llm=llm)


messages = [
    SystemMessage(content="You are a helpfull assistant"),
    HumanMessage(content="What is langchain?"),
]


response = model.invoke(messages)
messages.append(AIMessage(response.content))
print(messages)
