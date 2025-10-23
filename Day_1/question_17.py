"""
**Q17 - Streaming Response Handler**
Question: Create an async generator with Pydantic validation that handles streaming LLM responses and yields validated chunks.
Input: Streaming API response
Expected Output: Async generator of validated response chunks
Usage: Real-time streaming applications like chatbots with type safety
"""

import asyncio
from pydantic import BaseModel, Field, validator
from typing import AsyncGenerator, Optional

class StreamChunk(BaseModel):
    chunk_id: int
    content: str
    is_final: bool = False
    token_count: int
    
    @validator('content')
    def validate_content(cls, v):
        if not isinstance(v, str):
            raise ValueError('Content must be string')
        return v

async def mock_streaming_api() -> AsyncGenerator[str, None]:
    """Simulates streaming API response"""
    text = "This is a streaming response that comes in multiple chunks"
    words = text.split()
    
    for word in words:
        await asyncio.sleep(0.1)  # Simulate streaming delay
        yield word + " "

async def stream_with_validation() -> AsyncGenerator[StreamChunk, None]:
    """
    Async generator that validates and yields streaming chunks
    """
    chunk_id = 0
    total_content = []
    
    async for raw_chunk in mock_streaming_api():
        chunk_id += 1
        total_content.append(raw_chunk)
        
        validated_chunk = StreamChunk(
            chunk_id=chunk_id,
            content=raw_chunk,
            is_final=False,
            token_count=len(raw_chunk.split())
        )
        
        yield validated_chunk
    
    # Final chunk
    final_chunk = StreamChunk(
        chunk_id=chunk_id + 1,
        content="",
        is_final=True,
        token_count=len(''.join(total_content).split())
    )
    
    yield final_chunk

async def consume_stream():
    """Consumes and displays streaming response"""
    full_response = []
    total_tokens = 0
    
    async for chunk in stream_with_validation():
        if not chunk.is_final:
            print(chunk.content, end='', flush=True)
            full_response.append(chunk.content)
        else:
            total_tokens = chunk.token_count
            print(f"\n\n[Stream complete - Total tokens: {total_tokens}]")
    
    return ''.join(full_response)

# Test
result = asyncio.run(consume_stream())
