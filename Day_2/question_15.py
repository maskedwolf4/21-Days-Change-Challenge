"""
### Q15

**Question:** Design a Pydantic model `ChatMessage` with role validation (only "user", "assistant", "system" allowed), content string, and optional metadata dict with timestamp.

**Input:** `{"role": "user", "content": "Explain proteins", "metadata": {"user_id": "123"}}`

**Expected Output:** Validated ChatMessage object

**Usage:** Message validation in LLM chat applications and conversation history storage.
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Literal
from datetime import datetime

class ChatMessage(BaseModel):
    """Validate chat messages with role constraints"""
    role: Literal["user", "assistant", "system"]
    content: str = Field(..., min_length=1)
    metadata: Optional[Dict] = Field(default_factory=dict)
    
    @validator('metadata', pre=True, always=True)
    def add_timestamp(cls, v):
        """Automatically add timestamp if not present"""
        if v is None:
            v = {}
        if 'timestamp' not in v:
            v['timestamp'] = datetime.utcnow().isoformat()
        return v

# Usage
message = ChatMessage(
    role="user",
    content="Explain proteins",
    metadata={"user_id": "123"}
)
print(message.dict())
