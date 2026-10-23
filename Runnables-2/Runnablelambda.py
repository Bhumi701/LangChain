from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()

def word_count(text):
  return len(text.split())

# """runnable_word_counter = RunnableLambda(word_count)

# print(runnable_word_counter.invoke("hello ji que tal? hola! hOOOOOLEEE.."))"""

prompt = PromptTemplate(
  template='Write a joke about {topic}',
  input_varibales=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
  'joke': RunnablePassthrough(),
  'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({'topic':'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)