# LEGACY FILE - experimental prototype kept for reference only
# This demonstrates AgentOS with SQLite memory and MCP tools
# Not used in production system

from agno.agent import Agent
from agno.os import AgentOS
from agno.db.sqlite import SqliteDb
from agno.models.groq import Groq
from agno.tools.mcp import MCPTools
from agno.tools.hackernews import HackerNewsTools

agno_assist= Agent(
    name= "Agno Assist",
    model= Groq(id="openai/gpt-oss-120b"),
    db= SqliteDb(db_file="agno.db"),
    tools=[
        MCPTools(url="https://docs.agno.com/mcp"),
        HackerNewsTools(),
    ],
    add_datetime_to_context= True,
    add_history_to_context= True,
    num_history_runs= 3,
    instructions=[
        "Always use the get_top_hackernews_stories tool to fetch real data before responding.",
        "Never make up information. Only use data from the tool results.",
        "Write a report in bullet points."],
    markdown= True,
    debug_mode=True,    
)

agent_os= AgentOS(agents= [agno_assist], tracing= True)
app= agent_os.get_app() 

