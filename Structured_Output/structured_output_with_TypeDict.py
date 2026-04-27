from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
model = ChatHuggingFace(llm=llm)


# Schema
class Review(TypedDict):
    summary: Annotated[str, "A breif summary of the review"]
    sentiment: Annotated[
        str, "Return sentiment of the review either negative or positive"
    ]


structured_model = model.with_structured_output(Review)

response = structured_model.invoke(
    """I am not feeling good today because of my manager"""
)
print(response)
