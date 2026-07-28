from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
                model = 'text-embedding-3-large',
                    dimensions=32)

documnets = [
    "Delhi is the captial of India",
    "Paris is the captial of France",
    "Kolkata is the capital of West Bengal"
]
result = embedding.embed_documents(documnets)

print(str(result))
