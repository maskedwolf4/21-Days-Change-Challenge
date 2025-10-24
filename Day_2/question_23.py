"""
### Q23

**Question:** Create a FastAPI endpoint that accepts protein sequences via POST, validates them using Pydantic, performs async batch embedding generation, stores embeddings in a dictionary cache, and returns embedding vectors.

**Input:** `POST /embed {"sequences": ["MKTAY", "ACDEF"]}`

**Expected Output:** `{"embeddings": [[...], [...]], "cached": [false, false], "processing_time": 0.45}`

**Usage:** Protein embedding microservice for ML-based protein function prediction pipelines.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List
import asyncio
import time
import numpy as np

app = FastAPI()

# Pydantic models
class ProteinEmbeddingRequest(BaseModel):
    sequences: List[str] = Field(..., min_items=1, max_items=100)
    
    @validator('sequences')
    def validate_sequences(cls, v):
        for seq in v:
            if not seq or not all(c.upper() in 'ACDEFGHIKLMNPQRSTVWYX' for c in seq):
                raise ValueError(f"Invalid protein sequence: {seq}")
        return v

class EmbeddingResponse(BaseModel):
    embeddings: List[List[float]]
    cached: List[bool]
    processing_time: float

# Simple cache
embedding_cache = {}

async def generate_embedding(sequence: str):
    """Simulate async embedding generation"""
    await asyncio.sleep(0.1)  # Simulate API latency
    # Simple hash-based embedding (in production, use actual model)
    np.random.seed(hash(sequence) % (2**32))
    return np.random.rand(128).tolist()

@app.post("/embed", response_model=EmbeddingResponse)
async def embed_proteins(request: ProteinEmbeddingRequest):
    """Generate embeddings for protein sequences with caching"""
    start_time = time.time()
    
    embeddings = []
    cached_flags = []
    tasks = []
    
    for seq in request.sequences:
        if seq in embedding_cache:
            embeddings.append(embedding_cache[seq])
            cached_flags.append(True)
            tasks.append(None)
        else:
            cached_flags.append(False)
            tasks.append(generate_embedding(seq))
    
    # Generate embeddings for non-cached sequences
    new_embeddings = await asyncio.gather(*[t for t in tasks if t is not None])
    
    # Merge results
    new_idx = 0
    final_embeddings = []
    for i, seq in enumerate(request.sequences):
        if cached_flags[i]:
            final_embeddings.append(embeddings[i])
        else:
            emb = new_embeddings[new_idx]
            embedding_cache[seq] = emb
            final_embeddings.append(emb)
            new_idx += 1
    
    processing_time = time.time() - start_time
    
    return EmbeddingResponse(
        embeddings=final_embeddings,
        cached=cached_flags,
        processing_time=round(processing_time, 2)
    )

# Run with: uvicorn app:app --reload
