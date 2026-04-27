from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")

prompt1 = PromptTemplate(
    template="Generate a detailed report {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary for following \n {text}",
    input_variables=["text"],
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({"topic": "Unemployment"})
print(response)
chain.get_graph().print_ascii()
