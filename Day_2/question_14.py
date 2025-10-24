"""
### Q14

**Question:** Write an async function that concurrently fetches embeddings for multiple text chunks from an API, with retry logic and timeout handling.

**Input:** List of 100 text chunks, API endpoint URL

**Expected Output:** List of 100 embedding vectors in same order

**Usage:** Batch processing documents for vector database ingestion in production RAG systems.
"""

import asyncio
import aiohttp
from typing import List

async def fetch_embedding(session, text, api_url, retries=3):
    """Fetch single embedding with retry logic"""
    for attempt in range(retries):
        try:
            async with session.post(
                api_url, 
                json={"text": text},
                timeout=aiohttp.ClientTimeout(total=30)
            ) as response:
                response.raise_for_status()
                result = await response.json()
                return result['embedding']
        except asyncio.TimeoutError:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
        except aiohttp.ClientError as e:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)

async def batch_fetch_embeddings(texts: List[str], api_url: str):
    """Concurrently fetch embeddings for multiple texts"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_embedding(session, text, api_url) for text in texts]
        embeddings = await asyncio.gather(*tasks, return_exceptions=True)
        return embeddings

# Usage
texts = ["chunk 1", "chunk 2", "chunk 3"]
embeddings = asyncio.run(batch_fetch_embeddings(texts, "https://api.example.com/embed"))
