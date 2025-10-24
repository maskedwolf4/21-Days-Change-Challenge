"""
### Q13

**Question:** Create a Pydantic model `EmbeddingRequest` with fields for text (list of strings), model_name, and dimension, with validators ensuring text list is not empty and dimension is positive.

**Input:** `{"text": ["hello world"], "model_name": "voyage-2", "dimension": 1024}`

**Expected Output:** Validated EmbeddingRequest object or ValidationError

**Usage:** Request validation in vector embedding microservices for RAG applications.
"""

from pydantic import BaseModel, Field, validator
from typing import List

class EmbeddingRequest(BaseModel):
    """Validate embedding API requests"""
    text: List[str] = Field(..., min_items=1)
    model_name: str
    dimension: int = Field(..., gt=0)
    
    @validator('text')
    def validate_text_not_empty(cls, v):
        """Ensure text list is not empty and contains valid strings"""
        if not v:
            raise ValueError('Text list cannot be empty')
        if any(not isinstance(item, str) or not item.strip() for item in v):
            raise ValueError('All text items must be non-empty strings')
        return v
    
    @validator('dimension')
    def validate_dimension_positive(cls, v):
        """Ensure dimension is positive"""
        if v <= 0:
            raise ValueError('Dimension must be positive')
        return v

# Usage
try:
    request = EmbeddingRequest(
        text=["hello world"], 
        model_name="voyage-2", 
        dimension=1024
    )
    print(request)
except Exception as e:
    print(f"Validation error: {e}")
