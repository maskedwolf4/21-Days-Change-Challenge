"""
**Q25 - Rate-Limited Embeddings API**
Question: Implement a FastAPI service with rate limiting middleware that generates text embeddings, caches results, and handles concurrent requests with proper error handling.
Input: POST request with text list
Expected Output: Array of embedding vectors with request metadata
Usage: Building embedding services for RAG systems with cost and performance optimization
"""

from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List
import time
import hashlib
from datetime import datetime, timedelta
from collections import defaultdict
import asyncio

app = FastAPI(title="Embeddings Service with Rate Limiting")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmbeddingRequest(BaseModel):
    texts: List[str] = Field(..., min_items=1, max_items=100)
    model: str = Field(default="text-embedding-3-small")

class EmbeddingResponse(BaseModel):
    embeddings: List[List[float]]
    model: str
    total_tokens: int
    cached: List[bool]
    request_id: str

# Rate limiting storage (use Redis in production)
rate_limit_store = defaultdict(list)
RATE_LIMIT = 10  # requests per minute
RATE_WINDOW = 60  # seconds

# Embedding cache (use Redis in production)
embedding_cache = {}
CACHE_TTL = 3600  # 1 hour

class RateLimiter:
    """Token bucket rate limiter"""
    
    @staticmethod
    def check_rate_limit(client_id: str) -> bool:
        """Check if client has exceeded rate limit"""
        now = time.time()
        
        # Remove old requests outside window
        rate_limit_store[client_id] = [
            req_time for req_time in rate_limit_store[client_id]
            if now - req_time < RATE_WINDOW
        ]
        
        # Check if under limit
        if len(rate_limit_store[client_id]) >= RATE_LIMIT:
            return False
        
        # Add current request
        rate_limit_store[client_id].append(now)
        return True

def get_client_id(request: Request) -> str:
    """Extract client identifier from request"""
    # Use API key or IP address
    api_key = request.headers.get("X-API-Key")
    if api_key:
        return api_key
    return request.client.host

async def generate_embedding(text: str, model: str) -> List[float]:
    """
    Simulates embedding generation
    In production, call OpenAI/Cohere/etc API
    """
    await asyncio.sleep(0.1)  # Simulate API latency
    
    # Mock embedding (384 dimensions)
    # In production: openai.Embedding.create()
    embedding = [hash(text + str(i)) % 100 / 100.0 for i in range(384)]
    
    return embedding

def get_cache_key(text: str, model: str) -> str:
    """Generate cache key from text and model"""
    content = f"{model}:{text}"
    return hashlib.md5(content.encode()).hexdigest()

@app.post("/embeddings", response_model=EmbeddingResponse)
async def create_embeddings(
    request: EmbeddingRequest,
    http_request: Request,
    client_id: str = Depends(get_client_id)
):
    """
    Generate embeddings with rate limiting and caching
    """
    # Check rate limit
    if not RateLimiter.check_rate_limit(client_id):
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Please try again later."
        )
    
    embeddings = []
    cached_flags = []
    total_tokens = 0
    
    # Process each text
    for text in request.texts:
        cache_key = get_cache_key(text, request.model)
        
        # Check cache
        if cache_key in embedding_cache:
            cached_entry = embedding_cache[cache_key]
            
            # Check if cache is still valid
            if time.time() - cached_entry['timestamp'] < CACHE_TTL:
                embeddings.append(cached_entry['embedding'])
                cached_flags.append(True)
                total_tokens += cached_entry['tokens']
                continue
        
        # Generate new embedding
        embedding = await generate_embedding(text, request.model)
        tokens = len(text.split())
        
        # Store in cache
        embedding_cache[cache_key] = {
            'embedding': embedding,
            'tokens': tokens,
            'timestamp': time.time()
        }
        
        embeddings.append(embedding)
        cached_flags.append(False)
        total_tokens += tokens
    
    request_id = hashlib.md5(
        f"{client_id}{time.time()}".encode()
    ).hexdigest()[:12]
    
    return EmbeddingResponse(
        embeddings=embeddings,
        model=request.model,
        total_tokens=total_tokens,
        cached=cached_flags,
        request_id=request_id
    )

@app.get("/cache/stats")
async def get_cache_stats():
    """Get cache statistics"""
    return {
        "total_entries": len(embedding_cache),
        "cache_ttl_seconds": CACHE_TTL,
        "rate_limit_per_minute": RATE_LIMIT
    }

@app.delete("/cache/clear")
async def clear_cache():
    """Clear embedding cache"""
    embedding_cache.clear()
    return {"message": "Cache cleared successfully"}

# To test:
# curl -X POST "http://localhost:8000/embeddings" \
#   -H "Content-Type: application/json" \
#   -H "X-API-Key: test-key-123" \
#   -d '{"texts": ["Hello world", "Machine learning"]}'
