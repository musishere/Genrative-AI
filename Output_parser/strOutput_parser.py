from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
llm = HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = ChatHuggingFace(llm=llm)


template1 = PromptTemplate(template="Write a detailed report on {topic}")
