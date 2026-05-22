"""
TypedDict definitions for LangGraph state tracing.
"""
from typing import Annotated, TypedDict, List
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]  # full chat history
    intent: str          # "rag" | "weather" | "chitchat"
    query: str          # original user message
    retrieved_docs: List[dict]  # [{text, metadata}]
    plan: List[str]    # planner steps (may be [query])
    answer: str          # current answer being built
    confidence: float        # validator score 0.0–1.0
    hitl_required: bool         # True = graph must pause
    hitl_question: str          # clarification to show user
    thread_id: str          # checkpointer key
    error: str | None   # error message or None
