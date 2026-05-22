"""
RAG Agent utilizing hybrid retrieval.
"""
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from graph.state import AgentState
from retrieval.hybrid_retriever import HybridRetriever
from utils.config import settings
from utils.retry import llm_retry

# Maintain a persistent retriever instance
retriever = None

@llm_retry()
def rag_agent(state: AgentState):
    """Retrieve docs and generate answer."""
    global retriever
    if not retriever:
        retriever = HybridRetriever()

    query = state.get("query", "")
    
    docs = retriever.retrieve(query, top_k=5)
    
    if not docs:
        return {
            "answer": "I don't have information on this topic.",
            "retrieved_docs": [],
            "confidence": 0.0
        }
        
    context_chunks = [d["text"] for d in docs]
    context = "\n\n---\n\n".join(context_chunks)
    
    llm = ChatGroq(
        model=settings.llm_smart_model,
        temperature=0.2,
        api_key=settings.groq_api_key
    )
    
    system_prompt = (
        "You are a Knowledge Expert. Your task is to provide a comprehensive, clear, and "
        "well-structured explanation based on the provided context. "
        "Summarize the key points first, then dive into details if necessary. "
        "If the context is insufficient, explain what is missing. "
        "Always maintain an objective and professional tone."
    )
    user_prompt = f"Context:\n{context}\n\nQuestion: {query}"
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    response = llm.invoke(messages)
    
    return {
        "answer": response.content,
        "retrieved_docs": docs
    }
