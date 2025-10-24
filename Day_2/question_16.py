"""
### Q16

**Question:** Create an async function that processes a queue of text generation requests with rate limiting (max 5 concurrent requests) and aggregates results.

**Input:** Queue of 50 prompts, LLM API client

**Expected Output:** List of 50 generated responses with metadata (time taken, tokens used)

**Usage:** Batch inference in production LLM applications with cost and latency optimization.
"""

import asyncio
from typing import List, Dict
import time

async def generate_text(prompt: str, api_client):
    """Simulate LLM API call"""
    start = time.time()
    await asyncio.sleep(0.5)  # Simulate API latency
    tokens = len(prompt.split()) * 10
    return {
        "prompt": prompt,
        "response": f"Generated response for: {prompt[:30]}...",
        "time_taken": time.time() - start,
        "tokens_used": tokens
    }

async def process_queue_with_rate_limit(
    prompts: List[str], 
    api_client, 
    max_concurrent=5
):
    """Process prompts with concurrency limit"""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def limited_generate(prompt):
        async with semaphore:
            return await generate_text(prompt, api_client)
    
    tasks = [limited_generate(prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks)
    return results

# Usage
prompts = [f"Prompt {i}" for i in range(50)]
results = asyncio.run(process_queue_with_rate_limit(prompts, None, max_concurrent=5))
print(f"Processed {len(results)} prompts")
