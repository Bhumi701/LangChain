import os 
os.environ["OPENAI_API_KEY"] =""
#!pip install -q langchain-openai langchain-community langchain-core requests duckduckgo-search


from langchain_openai import ChatOpenAI 
from langchain_core.tools import tool
import requests 
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

@tool 
def get_weather_data(city:str) -> str:
  """This function fetches the current weather data for a given city"""
  
  url = f"...query={city}"
  response = requests.get(url)
  return response.json()


llm = ChatOpenAI()

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

#pull the ReAct prompt from langchain hub
prompt = hub.pull("hwchase17/react") #pulls the standard ReAct agent prompt


#create react agent manually with the pulled prompt
agent = create_react_agent(
  llm = llm,
  tools=[search_tool, get_weather_data],
  prompt = prompt
)

#wrap it with AgentExecutor
agent_executor = AgentExecutor(
  agent = agent,
  tools = [search_tool, get_weather_data],
  verbose=True
)

#invoke
response = agent_executor.invoke({"input": "Find the capital of Madhya Pradesh, then find it's current weather condition"})

print(response['output']) 
#The capital of Madhya Pradesh is Bhopal, and the current weather condition in Bhopal is partly cloudy with a temperature of 40°C