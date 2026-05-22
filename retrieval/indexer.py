"""
Idempotent script to seed ChromaDB and BM25 store from hardcoded RAG chunks.
"""
import os
import pickle
import chromadb
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.config import settings

DOCS = [
    {"id":"doc1", "text":"LangGraph is a library for building stateful multi-agent applications using graph-based workflows. It supports checkpointing, human-in-the-loop, and streaming.", "metadata":{"topic":"langgraph"}},
    {"id":"doc2", "text":"RAG (Retrieval Augmented Generation) combines a retrieval system with an LLM. Documents are indexed into a vector store and retrieved by semantic similarity.", "metadata":{"topic":"rag"}},
    {"id":"doc3", "text":"BM25 is a sparse retrieval algorithm based on term frequency. It works well for keyword-heavy queries and complements dense vector search.", "metadata":{"topic":"retrieval"}},
    {"id":"doc4", "text":"ChromaDB is an open-source vector database that runs locally. It stores embeddings and supports similarity search with metadata filtering.", "metadata":{"topic":"chromadb"}},
    {"id":"doc5", "text":"FastAPI is a modern Python web framework for building APIs. It supports async, automatic docs, and Pydantic validation out of the box.", "metadata":{"topic":"fastapi"}},
    {"id":"doc6", "text":"BPMN (Business Process Model and Notation) is a graphical standard for modeling business workflows. IVR flows can be modelled as BPMN diagrams with decision gateways.", "metadata":{"topic":"bpmn"}},
    {"id":"doc7", "text":"Hybrid retrieval combines sparse (BM25) and dense (vector) search using Reciprocal Rank Fusion (RRF). RRF merges ranked lists with score = 1/(k + rank) where k=60.", "metadata":{"topic":"retrieval"}},
    {"id":"doc8", "text":"Human-in-the-loop (HITL) in LangGraph allows a graph to pause mid-execution, save state to a checkpointer, and resume after receiving human input.", "metadata":{"topic":"hitl"}}
]

def main():
    print("=== Indexing Started ===")
    os.makedirs(os.path.dirname(settings.chroma_path) or ".", exist_ok=True)
    
    print("[1/4] Connecting to ChromaDB...")
    client = chromadb.PersistentClient(path=settings.chroma_path)
    
    try:
        client.delete_collection(settings.chroma_collection)
    except Exception:
        pass
        
    collection = client.create_collection(name=settings.chroma_collection)
    
    print("[2/4] Initializing Embeddings (sentence-transformers)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    print("[3/4] Storing in ChromaDB...")
    texts = [d["text"] for d in DOCS]
    embeddings = model.encode(texts).tolist()
    
    collection.add(
         ids=[d["id"] for d in DOCS],
         embeddings=embeddings,
         documents=texts,
         metadatas=[d["metadata"] for d in DOCS]
    )
    
    print("[4/4] Building BM25 Index...")
    tokenized = [doc.lower().split() for doc in texts]
    bm25 = BM25Okapi(tokenized)
    
    os.makedirs(os.path.dirname(settings.bm25_index_path) or ".", exist_ok=True)
    with open(settings.bm25_index_path, "wb") as f:
        pickle.dump(bm25, f)
        
    print("✓ Indexing complete.")

if __name__ == "__main__":
    main()
