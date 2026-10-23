from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

prompt = PromptTemplate(
  template='Answer the following question \n {question} from the following text -\n {text}',
  input_variables = ['question', 'text']
)

parser = StrOutputParser()

url = 'https://www.blancpain.com/en/villeret/villeret-carrousel-repetition-minutes-chronographe-flyback-2358-3631-55b'
loader =WebBaseLoader(url)

docs = loader.lazy_load()

chain = prompt | model | parser


for doc in docs:
  print(chain.invoke({
    'question': 'What is the price of this product', 
    'text': doc.page_content
    
  }))