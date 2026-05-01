from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel


load_dotenv()

prompt_1 = PromptTemplate(
    template="Write a tweet about {topic}", input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template="Write a Linkedin post about {topic}", input_variables=["topic"]
)

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt_1, model, parser),
        "post": RunnableSequence(prompt_2, model, parser),
    }
)

response = parallel_chain.invoke({"topic": "AI"})
print(response["tweet"])
