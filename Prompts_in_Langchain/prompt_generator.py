from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
    You are an expert research assistant.
    Summarize the research paper "{paper_input}" in a "{style_input}" tone.
    Keep the response "{length_input}".
    Address the user’s request: "{userinput}".
    Use clear, accurate language and avoid unrelated details.
    """,
    input_variables=["paper_input", "style_input", "length_input", "userinput"],
)


template.save("template.json")
