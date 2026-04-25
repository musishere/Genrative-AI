from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

data = TextLoader(
    "/Users/macbookpro/Documents/Genrative AI/RAG/Document_Loaders/notes.txt"
)
docs = data.load()

template = ChatPromptTemplate(
    [("system", "You are the AI that summarize's the text"), ("human", "{data}")]
)
prompt = template.format_messages(data=docs[0].page_content)

model = ChatMistralAI(model="mistral-small2506")
response = model.invoke("What is Langchain?")
print(response)
