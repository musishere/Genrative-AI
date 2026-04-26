from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage


chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpul {domain} expert"),
        ("human", "explain in simple terms what is {topic}"),
    ]
)


prompt = chat_template.invoke({"domain": "Cricket", "topic": "Dosra"})
print(prompt)
