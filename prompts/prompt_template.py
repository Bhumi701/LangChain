from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=os.getenv("GOOGLE_API_KEY"))

template2 = PromptTemplate(
  template='Greet this person in 5 languages including spanish. The person is {name}.',
  input_variables = ['name']
)

prompt = template2.invoke({'name': 'bhumi'})
result = model.invoke(prompt)
print(result.content)