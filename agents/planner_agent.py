"""
Planner Agent determining multi-step execution logic.
"""
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from graph.state import AgentState
from utils.config import settings
from utils.retry import llm_retry

@llm_retry()
def planner_agent(state: AgentState):
    """Splits queries internally."""
    query = state.get("query", "")
    
    indicator_words = ["and", "also", "then", "plus", "as well", "additionally", ","]
    query_lower = query.lower()
    
    needs_split = any(word in query_lower for word in indicator_words)
    
    if not needs_split:
        return {"plan": [query]}
        
    llm = ChatGroq(
        model=settings.llm_fast_model,
        temperature=0.0,
        api_key=settings.groq_api_key
    )
    
    prompt = f"Break this query into ordered sub-questions, one per line, numbered. No explanations.\nQuery: {query}"
    messages = [HumanMessage(content=prompt)]
    
    response = llm.invoke(messages)
    
    steps = []
    lines = response.content.split("\n")
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            parts = cleaned.split(". ", 1)
            steps.append(parts[1] if len(parts) == 2 else cleaned)
            
    if not steps:
        steps = [query]
        
    return {"plan": steps}
