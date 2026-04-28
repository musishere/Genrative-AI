from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt_1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template="Explain the following joke - {text}", input_variables=["text"]
)


llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()


chain = RunnableSequence(prompt_1, model, parser, prompt_2, model, parser)
print(chain.invoke({"topic": "AI"}))
