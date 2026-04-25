from langchain_community.document_loaders import TextLoader

data = TextLoader(
    "/Users/macbookpro/Documents/Genrative AI/RAG/Document_Loaders/notes.txt"
)
docs = data.load()
# print({"Docs":docs[0].page_content})
print(len(docs))
