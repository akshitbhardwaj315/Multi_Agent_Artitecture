"""
Validator Agent checking the answer grounding against context.
"""
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from graph.state import AgentState
from utils.config import settings
from utils.retry import llm_retry

@llm_retry()
def validator_agent(state: AgentState):
    """Validates answer against context constraint."""
    docs = state.get("retrieved_docs", [])
    query = state.get("query", "")
    answer = state.get("answer", "")
    
    if not docs:
        return {
            "confidence": 0.0,
            "hitl_required": True,
            "hitl_question": "Could you clarify what you're looking for?"
        }
        
    context_text = "\n".join([d["text"] for d in docs])[:500]
    
    llm = ChatGroq(
        model=settings.llm_fast_model,
        temperature=0.0,
        api_key=settings.groq_api_key
    )
    
    prompt = (
        "Rate how well this answer is grounded in the provided context.\n"
        "Reply with ONLY a decimal number between 0.0 and 1.0.\n"
        "0.0 = completely ungrounded, 1.0 = perfectly grounded.\n\n"
        f"Context: {context_text}\n\nAnswer: {answer}"
    )
    
    messages = [HumanMessage(content=prompt)]
    response = llm.invoke(messages)
    
    try:
        conf_str = response.content.strip()
        confidence = float(conf_str)
        confidence = max(0.0, min(1.0, confidence))
    except (ValueError, TypeError):
        confidence = 0.5
        
    hitl_required = confidence < settings.validator_confidence_threshold
    
    if hitl_required:
        hitl_question = f"I'm not fully confident about this. Could you clarify what aspect of '{query}' you need most?"
    else:
        hitl_question = ""
        
    return {
        "confidence": confidence,
        "hitl_required": hitl_required,
        "hitl_question": hitl_question
    }
