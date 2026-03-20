# LEGACY FILE - kept for reference only
# This is the original standalone script. The production version is in agents/hackernews_agent.py

from typing import Iterator
from agno.agent import Agent, RunOutputEvent, RunEvent, RunOutput
from agno.models.groq import Groq
from agno.tools.hackernews import HackerNewsTools
from agno.utils.pprint import pprint_run_response
from  dotenv import load_dotenv

load_dotenv()

agent= Agent(
    model= Groq(id="openai/gpt-oss-120b"),
    tools=[HackerNewsTools()],
    instructions="Write a Report on the topic, Output only the report and a user friendly way in points",
    markdown= True,

)
#----------------------option 1 for custom Streaming***

# stream: Iterator[RunOutputEvent] = agent.run("Trending products", stream= True)
# for chunk in stream:
#     if chunk.event == RunEvent.run_content:
#         print(chunk.content)

#----------------------option 2 for fast output in terminal and beautiful***

response= RunOutput= agent.run("Trending news in AI tech tell me in 5 lines only hardly 100 words allowed", stream=True)
pprint_run_response(response, markdown=True)

