from langchain_community.document_loaders import TextLoader

loader = TextLoader("/Users/macbookpro/Documents/Genrative AI/LangChain_Document_Loaders/random_text.txt",encoding='utf-8')

docs = loader.load()
print(docs[0])