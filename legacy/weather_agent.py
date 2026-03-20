# LEGACY FILE - kept for reference only
# This is the original standalone script. The production version is in agents/weather_agent.py

from agno.agent import Agent, RunOutput
from agno.models.groq import Groq
from tools.weather_tool import WeatherTools
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv

load_dotenv()

agent= Agent(
    id= "weather-agent",
    model= Groq(id="openai/gpt-oss-120b"),
    name= "Weather agent",
    role= "get weather reports for any city and first greet with Hey Akshit with emoji and nicely then give an output ",
    tools=[WeatherTools()],
    markdown= True,

)

response = agent.run("What is the weather in hulululu right now?", stream=True)
pprint_run_response(response, markdown=True)

