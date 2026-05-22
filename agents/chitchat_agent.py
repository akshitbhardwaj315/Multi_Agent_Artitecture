"""
Chitchat fallback agent.
"""
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from graph.state import AgentState
from utils.config import settings
from utils.retry import llm_retry

@llm_retry()
def chitchat_agent(state: AgentState):
    """Direct LLM chat with simple history."""
    query = state.get("query", "")
    messages_history = state.get("messages", [])
    
    llm = ChatGroq(
        model=settings.llm_fast_model,
        temperature=0.7,
        api_key=settings.groq_api_key
    )
    
    system_prompt = (
        "You are a sophisticated, friendly, and highly intelligent AI assistant. "
        "Your goal is to provide helpful, clear, and well-reasoned responses. "
        "When appropriate, explain your reasoning or provide context to help the user understand. "
        "Maintain a professional yet approachable tone."
    )
    
    sys_msg = SystemMessage(content=system_prompt)
    
    recent = messages_history[-10:] if messages_history else []
    
    messages = [sys_msg] + recent
    
    if not recent or getattr(recent[-1], "content", None) != query:
        messages.append(HumanMessage(content=query))
    
    response = llm.invoke(messages)
    
    return {"answer": response.content}
