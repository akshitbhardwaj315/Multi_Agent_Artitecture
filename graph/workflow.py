"""
LangGraph workflow compilation.

Topology:
  START → master → [rag → planner → validator] | weather | chitchat → END
"""
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
import aiosqlite
import asyncio
import os

from graph.state import AgentState
from agents.master_agent import master_agent
from agents.rag_agent import rag_agent
from agents.planner_agent import planner_agent
from agents.validator_agent import validator_agent
from agents.weather_agent import weather_agent
from agents.chitchat_agent import chitchat_agent
from utils.config import settings


def route_from_master(state: AgentState) -> str:
    """Conditional edge: route by intent set by master agent."""
    intent = state.get("intent", "chitchat")
    if intent == "rag":
        return "rag"
    elif intent == "weather":
        return "weather"
    return "chitchat"


def _build_workflow() -> StateGraph:
    """Assemble the StateGraph (nodes + edges). No checkpointer here."""
    wf = StateGraph(AgentState)

    wf.add_node("master", master_agent)
    wf.add_node("rag", rag_agent)
    wf.add_node("planner", planner_agent)
    wf.add_node("validator", validator_agent)
    wf.add_node("weather", weather_agent)
    wf.add_node("chitchat", chitchat_agent)

    wf.add_edge(START, "master")
    wf.add_conditional_edges(
        "master",
        route_from_master,
        {"rag": "rag", "weather": "weather", "chitchat": "chitchat"},
    )
    wf.add_edge("rag", "planner")
    wf.add_edge("planner", "validator")
    wf.add_edge("validator", END)
    wf.add_edge("weather", END)
    wf.add_edge("chitchat", END)

    return wf


_graph = None
_conn = None

async def get_graph():
    """Singleton pattern to return the compiled graph with an async checkpointer."""
    global _graph, _conn
    if _graph is None:
        os.makedirs(os.path.dirname(settings.checkpoint_db_path) or "data", exist_ok=True)
        # Persistent async connection for the checkpointer
        _conn = await aiosqlite.connect(settings.checkpoint_db_path)
        checkpointer = AsyncSqliteSaver(_conn)
        
        # Compile workflow
        _graph = _build_workflow().compile(checkpointer=checkpointer)
    return _graph