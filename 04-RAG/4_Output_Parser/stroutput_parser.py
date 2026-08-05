from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# llm = HuggingFaceEndpoint(
#    repo_id="TinyLlama/TinyLlama-1.1B-chat-v1.0",
#    task="text-generation")

# model = ChatHuggingFace(llm=llm)

# 1st prompt --> detailed report
template1 = PromptTemplate(
    template='Write a deatiled report on {topic}',
    input_variables=['topic']
)

# 2nd prompt --> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'blackhole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)