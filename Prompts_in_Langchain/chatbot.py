from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

chat_history = [
    SystemMessage(content="You are a helpfull assistant"),
]
llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
model = ChatHuggingFace(llm=llm)


while True:
    user_input = input("You: ")

    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print("AI:", response.content)

print(chat_history)
