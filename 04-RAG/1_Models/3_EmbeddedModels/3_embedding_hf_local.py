from langchain_huggingface import HuggingFaceEmbeddings

import os
os.environ['HF_HOME'] = 'H:/huggingface_cache'

embedding = HuggingFaceEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2"
)

text = "delhi is the captial of India"

# same for documents
result = embedding.embed_query(text)

print(str(result))