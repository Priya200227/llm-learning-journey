from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# ChatPromptTemplate.from_messages([]) will a also give the same output

# Dynamic messages using ChatPromptTemplate
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
    # SystemMessage(content='You are a helpful {domain} expert'),
    # HumanMessage(content='Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain': 'dataanalyst', 'topic': 'Correlation'})

print(prompt)