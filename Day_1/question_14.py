"""
**Q14 - Async Document Embedding Pipeline**
Question: Build an async pipeline that chunks documents, generates embeddings concurrently, and validates output using Pydantic schemas.
Input: List of document texts, chunk size, embedding model name
Expected Output: List of validated embedding objects with metadata
Usage: Building RAG systems with efficient document processing
"""
import asyncio
from pydantic import BaseModel, Field, validator
from typing import List, Optional
import hashlib

class Document(BaseModel):
    text: str
    doc_id: str
    metadata: dict = Field(default_factory=dict)

class DocumentChunk(BaseModel):
    chunk_text: str
    chunk_id: str
    doc_id: str
    chunk_index: int
    
    @validator('chunk_text')
    def validate_chunk_length(cls, v):
        if len(v) < 10:
            raise ValueError('Chunk too short')
        return v

class EmbeddingResult(BaseModel):
    chunk_id: str
    embedding: List[float]
    model_name: str
    dimensions: int

async def chunk_document(doc: Document, chunk_size: int) -> List[DocumentChunk]:
    """Chunks document into smaller pieces"""
    chunks = []
    text = doc.text
    words = text.split()
    
    for i in range(0, len(words), chunk_size):
        chunk_words = words[i:i + chunk_size]
        chunk_text = ' '.join(chunk_words)
        chunk_id = hashlib.md5(chunk_text.encode()).hexdigest()[:8]
        
        chunks.append(DocumentChunk(
            chunk_text=chunk_text,
            chunk_id=chunk_id,
            doc_id=doc.doc_id,
            chunk_index=i // chunk_size
        ))
    
    return chunks

async def generate_embedding(chunk: DocumentChunk, model_name: str = "mock-model") -> EmbeddingResult:
    """Simulates async embedding generation"""
    await asyncio.sleep(0.3)
    
    # Mock embedding (in reality, call embedding API)
    embedding = [0.1] * 384  # Mock 384-dimensional embedding
    
    return EmbeddingResult(
        chunk_id=chunk.chunk_id,
        embedding=embedding,
        model_name=model_name,
        dimensions=len(embedding)
    )

async def process_document_pipeline(documents: List[Document], chunk_size: int = 100):
    """Full async pipeline for document processing"""
    all_embeddings = []
    
    for doc in documents:
        # Chunk document
        chunks = await chunk_document(doc, chunk_size)
        
        # Generate embeddings concurrently
        tasks = [generate_embedding(chunk) for chunk in chunks]
        embeddings = await asyncio.gather(*tasks)
        
        all_embeddings.extend(embeddings)
    
    return [emb.dict() for emb in all_embeddings]

# Test
docs = [
    Document(text="Machine learning is a subset of artificial intelligence " * 20, doc_id="doc1"),
    Document(text="Natural language processing enables computers to understand text " * 20, doc_id="doc2")
]

results = asyncio.run(process_document_pipeline(docs, chunk_size=50))
print(f"Generated {len(results)} embeddings")
print(f"Sample: {results[0]}")
