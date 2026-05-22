"""
Master Agent routing to exactly one intent: rag, weather, chitchat.
"""
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from graph.state import AgentState
from utils.config import settings
from utils.retry import llm_retry

@llm_retry()
def master_agent(state: AgentState):
    """Classifies user intent."""
    query = state.get("query", "")
    
    llm = ChatGroq(
        model=settings.llm_fast_model,
        temperature=0.0,
        api_key=settings.groq_api_key
    )
    
    system_prompt = (
        "Classify the user query into exactly one word.\n"
        "Reply with only one of: rag, weather, chitchat\n"
        "- rag: questions about documents, knowledge, how things work\n"
        "- weather: any question about weather or temperature\n"
        "- chitchat: greetings, jokes, personal questions, anything else\n"
        "Do not explain. Output only the single word."
    )
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query)
    ]
    
    response = llm.invoke(messages)
    content = response.content.strip().lower()
    
    intent = content if content in ["rag", "weather", "chitchat"] else "chitchat"
    
    return {"intent": intent, "query": query}
