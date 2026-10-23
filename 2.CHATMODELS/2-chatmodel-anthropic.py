from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3.5-sonnet-20241022')

result = model.invoke("What is the capital of France?")
print(result) #ans+token extra data mtlb meta ata v dedeta h so
print(result.content)