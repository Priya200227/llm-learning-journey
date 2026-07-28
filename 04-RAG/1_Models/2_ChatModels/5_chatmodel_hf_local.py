from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# By default it files are stored in C drive, and if we want to store in other drive
import os
os.environ['HF_HOME'] = 'H:/huggingface_cache'

# Now when you run it will download into the local RAM
# And if you have GPU it will run fast
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
        )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is AI?")

print(result.content)
