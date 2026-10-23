from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 

#chat_template = ChatPromptTemplate([SystemMessage(content="You are a helpfl {domain} assistant."),HumanMessage(content="Tell me more about {topic}.")])

chat_template = ChatPromptTemplate([
  ('system', 'You are a helpful {domain} assistant.'),
  ('human', 'Tell me more about {topic}.')
])

prompt = chat_template.invoke({'domain': 'research', 'topic': 'langchain'})

print(prompt)