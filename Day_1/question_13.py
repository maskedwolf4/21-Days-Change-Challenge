"""
**Q13 - Async LLM Batch Inference**
Question: Create an async function that processes multiple prompts concurrently using asyncio, with Pydantic models for request/response validation.
Input: List of prompts, max concurrent requests
Expected Output: List of validated LLM responses
Usage: Parallel processing of LLM requests in production AI applications
"""
import asyncio
from pydantic import BaseModel, Field
from typing import List

class LLMRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    temperature: float = Field(default=0.7, ge=0, le=2)
    max_tokens: int = Field(default=100, gt=0)

class LLMResponse(BaseModel):
    prompt: str
    completion: str
    tokens_used: int

async def mock_llm_call(request: LLMRequest) -> LLMResponse:
    """Simulates async LLM API call"""
    await asyncio.sleep(0.5)  # Simulate API latency
    return LLMResponse(
        prompt=request.prompt,
        completion=f"Generated response for: {request.prompt[:30]}...",
        tokens_used=len(request.prompt.split()) * 2
    )

async def batch_inference(prompts: List[str], max_concurrent: int = 3):
    """Process multiple prompts concurrently with semaphore"""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def process_with_limit(prompt):
        async with semaphore:
            request = LLMRequest(prompt=prompt)
            return await mock_llm_call(request)
    
    tasks = [process_with_limit(prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks)
    
    return [result.dict() for result in results]

# Test
prompts = [
    "Explain quantum computing",
    "What is machine learning?",
    "Describe neural networks",
    "How does NLP work?"
]

results = asyncio.run(batch_inference(prompts, max_concurrent=2))
for result in results:
    print(result)
