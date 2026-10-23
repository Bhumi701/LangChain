from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational"
)

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template="Say hello to {name} in a friendly way",
    input_variables=["name"]
)

prompt = template.invoke({"name": "Bhumi"})
result = model.invoke(prompt)

print(result.content)




















import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"],
)

completion = client.chat.completions.create(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)
