"""
Hybrid Retriever leveraging RRF logic over local ChromaDB and BM25 index.
"""
import pickle
import chromadb
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from utils.config import settings
from retrieval.indexer import DOCS

class HybridRetriever:
    def __init__(self):
        try:
            with open(settings.bm25_index_path, "rb") as f:
                self.bm25 = pickle.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Run: python retrieval/indexer.py")
        
        self.client = chromadb.PersistentClient(path=settings.chroma_path)
        self.collection = self.client.get_collection(name=settings.chroma_collection)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.doc_texts = [d["text"] for d in DOCS]
        self.doc_metadatas = [d["metadata"] for d in DOCS]

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Retrieve using BM25 and ChromaDB, fused via RRF."""
        # 1. BM25 Sparse
        tokens = query.lower().split()
        bm25_scores = self.bm25.get_scores(tokens)
        bm25_ranked = sorted(enumerate(bm25_scores), key=lambda x: x[1], reverse=True)
        bm25_rank = {idx: rank + 1 for rank, (idx, _) in enumerate(bm25_ranked)}
        
        # 2. ChromaDB Dense
        query_embedding = self.model.encode(query).tolist()
        total_docs = len(self.doc_texts)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=min(top_k * 2, total_docs)
        )
        
        dense_ranked = {}
        id_to_idx = {d["id"]: i for i, d in enumerate(DOCS)}
        for rank, doc_id in enumerate(results["ids"][0]):
            idx = id_to_idx[doc_id]
            dense_ranked[idx] = rank + 1
            
        # 3. RRF Fusion (k=60)
        rrf_scores = []
        for doc_idx in range(total_docs):
            score = 0
            if doc_idx in bm25_rank:
                score += 1 / (60 + bm25_rank[doc_idx])
            if doc_idx in dense_ranked:
                score += 1 / (60 + dense_ranked[doc_idx])
            rrf_scores.append((doc_idx, score))
            
        # 4. Sort and return
        rrf_scores.sort(key=lambda x: x[1], reverse=True)
        top_results = []
        for doc_idx, score in rrf_scores[:top_k]:
            if score > 0:
                top_results.append({
                    "text": self.doc_texts[doc_idx],
                    "metadata": self.doc_metadatas[doc_idx],
                    "score": score
                })
        return top_results
