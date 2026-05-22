import httpx
import asyncio
import json
import uuid

BASE_URL = "http://localhost:8000"

TEST_QUERIES = [
    # 1-5: Easy (Greetings & Chitchat)
    "Hello there!",
    "Who are you?",
    "Tell me a joke.",
    "What is the meaning of life?",
    "Can you help me with something?",

    # 6-12: Medium (Weather & Knowledge)
    "What is the weather in Mumbai?",
    "How is the temperature in Delhi?",
    "Tell me about Bangalore weather.",
    "What is LangGraph?",
    "How does RAG work?",
    "What is ChromaDB?",
    "Explain BM25 retrieval.",

    # 13-20: Complex (Deep Knowledge & Multi-turn potential)
    "Explain how Hybrid Retrieval combines sparse and dense search.",
    "What is Human-in-the-loop (HITL) in the context of agent workflows?",
    "Tell me about BPMN and its relation to IVR flows.",
    "How does Reciprocal Rank Fusion (RRF) calculate scores?",
    "Why would I use LangGraph instead of a simple linear chain?",
    "What are the benefits of using FastAPI for agentic APIs?",
    "Can you explain the difference between vector search and keyword search?",
    "Does this system support checkpointing? How?"
]

async def run_test(query: str):
    thread_id = str(uuid.uuid4())
    print(f"\n[QUERY]: {query}")
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                f"{BASE_URL}/chat/stream",
                json={"message": query, "thread_id": thread_id, "stream": False}
            )
            if response.status_code == 200:
                data = response.json()
                print(f"[INTENT]: {data.get('intent')}")
                # Print only first 100 chars of answer for brevity
                answer = data.get('answer', '')
                print(f"[ANSWER]: {answer[:150]}...")
                return True
            else:
                print(f"[ERROR]: Status {response.status_code}")
                return False
        except Exception as e:
            print(f"[EXCEPTION]: {e}")
            return False

async def main():
    print("=== Starting 20-Query Integration Test ===")
    success_count = 0
    for q in TEST_QUERIES:
        if await run_test(q):
            success_count += 1
    
    print(f"\n=== Test Completed: {success_count}/{len(TEST_QUERIES)} succeeded ===")

if __name__ == "__main__":
    asyncio.run(main())
