#llm

from langchain_openai import OpenAI
from dotenv import load_dotenv #yh secret key ko load karne ke liye

load_dotenv()

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.9,max_completion_tokens=100) #temperature is for randomness in the output, creativity parameter, 0.9 means high randomness, 0.1 means low randomness =yh 0 to 2 tk hoti h. response mein 100 word chahiye
result = llm.invoke("What is the capital of France?")
print(result)