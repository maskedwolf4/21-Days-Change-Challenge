"""
**Q16 - Async Multi-Model Inference Router**
Question: Build an async router that sends requests to different LLM providers based on task type, with Pydantic request/response models and retry logic.
Input: Task type, prompt, provider preferences
Expected Output: Validated response from appropriate provider
Usage: Multi-model AI systems with fallback strategies
"""

import asyncio
from pydantic import BaseModel, Field
from typing import Literal, Optional
from enum import Enum

class TaskType(str, Enum):
    SUMMARIZATION = "summarization"
    TRANSLATION = "translation"
    CODE_GENERATION = "code_generation"
    QA = "question_answering"

class InferenceRequest(BaseModel):
    task_type: TaskType
    prompt: str
    provider_preference: Optional[list] = Field(default=["openai", "anthropic", "cohere"])
    max_retries: int = Field(default=3, ge=1, le=5)

class InferenceResponse(BaseModel):
    task_type: TaskType
    result: str
    provider_used: str
    attempt_number: int
    success: bool

class ModelRouter:
    """Routes requests to appropriate LLM provider with fallback"""
    
    def __init__(self):
        self.provider_configs = {
            "openai": {"endpoint": "api.openai.com", "models": {"summarization": "gpt-4"}},
            "anthropic": {"endpoint": "api.anthropic.com", "models": {"summarization": "claude-3"}},
            "cohere": {"endpoint": "api.cohere.ai", "models": {"summarization": "command"}}
        }
    
    async def call_provider(self, provider: str, request: InferenceRequest) -> str:
        """Simulates async call to specific provider"""
        await asyncio.sleep(0.5)
        
        # Simulate occasional failures
        import random
        if random.random() < 0.3:  # 30% failure rate for demo
            raise Exception(f"{provider} API error")
        
        return f"[{provider}] Response for {request.task_type.value}: {request.prompt[:30]}..."
    
    async def route_with_retry(self, request: InferenceRequest) -> InferenceResponse:
        """Routes request with retry logic across providers"""
        
        for attempt in range(1, request.max_retries + 1):
            for provider in request.provider_preference:
                try:
                    result = await self.call_provider(provider, request)
                    
                    return InferenceResponse(
                        task_type=request.task_type,
                        result=result,
                        provider_used=provider,
                        attempt_number=attempt,
                        success=True
                    )
                except Exception as e:
                    print(f"Attempt {attempt}: {provider} failed - {e}")
                    continue
        
        # All attempts failed
        return InferenceResponse(
            task_type=request.task_type,
            result="All providers failed",
            provider_used="none",
            attempt_number=request.max_retries,
            success=False
        )

async def process_multiple_tasks(requests: list):
    """Process multiple requests concurrently"""
    router = ModelRouter()
    tasks = [router.route_with_retry(req) for req in requests]
    results = await asyncio.gather(*tasks)
    return results

# Test
requests = [
    InferenceRequest(task_type=TaskType.SUMMARIZATION, prompt="Summarize this long article..."),
    InferenceRequest(task_type=TaskType.TRANSLATION, prompt="Translate to French..."),
    InferenceRequest(task_type=TaskType.CODE_GENERATION, prompt="Generate Python function...")
]

results = asyncio.run(process_multiple_tasks(requests))
for result in results:
    print(f"\nTask: {result.task_type}")
    print(f"Provider: {result.provider_used}")
    print(f"Success: {result.success}")
