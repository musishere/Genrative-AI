from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()


prompt = PromptTemplate(
    template = 'Generate a summary for text {text}',
    input_variables=['text']
)
loader = TextLoader("/Users/macbookpro/Documents/Genrative AI/LangChain_Document_Loaders/random_text.txt",encoding='utf-8')

docs = loader.load()
chain = prompt | model | parser
response = chain.invoke({'text':docs[0].page_content})
print(response)