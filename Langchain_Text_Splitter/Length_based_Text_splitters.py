from langchain.text_splitter import CharacterTextSplitter

random_text = """
Random Text File
================

Generated on: 2026-05-01T00:00:00Z
Identifier: a1b2c3d4-e5f6-7890-abcd-ef1234567890

The quick brown fox jumps over the lazy dog.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.

Random paragraph:
Sitting on a copper bench, the clock chimed thirteen times as the old radio hummed a forgotten tune. Somewhere between the sidewalks and the stars, a single idea decided to bloom into a thousand possibilities.

Lines of seeded randomness:
- 47f2b6c1
- 9a3e7d5b
- 2c8f0a11

End of file.
"""

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_text(text=random_text)
print(result)