"""
**Q24 - Async Batch Prediction Service**
Question: Build a FastAPI endpoint that accepts batch prediction requests, processes them asynchronously using background tasks, and provides status/result retrieval endpoints.
Input: POST with batch data, GET for status check
Expected Output: Job ID and batch predictions when complete
Usage: High-throughput prediction services for large-scale data processing
"""

from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import asyncio
import uuid
from datetime import datetime
from enum import Enum

app = FastAPI(title="Batch Prediction Service")

class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class BatchPredictionRequest(BaseModel):
    data: List[List[float]] = Field(..., min_items=1)
    callback_url: Optional[str] = None

class BatchJobResponse(BaseModel):
    job_id: str
    status: JobStatus
    submitted_at: str
    total_samples: int

class BatchResultResponse(BaseModel):
    job_id: str
    status: JobStatus
    predictions: Optional[List[float]] = None
    completed_at: Optional[str] = None
    error: Optional[str] = None

# In-memory job store (use Redis/database in production)
job_store: Dict[str, Dict] = {}

async def process_batch_prediction(job_id: str, data: List[List[float]]):
    """Background task for batch prediction"""
    try:
        # Update status to processing
        job_store[job_id]['status'] = JobStatus.PROCESSING
        
        predictions = []
        
        # Simulate prediction for each sample
        for sample in data:
            await asyncio.sleep(0.1)  # Simulate inference time
            prediction = sum(sample) / len(sample) * 2.5
            predictions.append(prediction)
        
        # Update job with results
        job_store[job_id].update({
            'status': JobStatus.COMPLETED,
            'predictions': predictions,
            'completed_at': datetime.now().isoformat()
        })
        
    except Exception as e:
        job_store[job_id].update({
            'status': JobStatus.FAILED,
            'error': str(e),
            'completed_at': datetime.now().isoformat()
        })

@app.post("/batch/predict", response_model=BatchJobResponse)
async def submit_batch_prediction(
    request: BatchPredictionRequest,
    background_tasks: BackgroundTasks
):
    """
    Submit batch prediction job
    """
    job_id = str(uuid.uuid4())
    
    # Initialize job
    job_store[job_id] = {
        'status': JobStatus.PENDING,
        'submitted_at': datetime.now().isoformat(),
        'total_samples': len(request.data),
        'predictions': None
    }
    
    # Add to background tasks
    background_tasks.add_task(process_batch_prediction, job_id, request.data)
    
    return BatchJobResponse(
        job_id=job_id,
        status=JobStatus.PENDING,
        submitted_at=job_store[job_id]['submitted_at'],
        total_samples=len(request.data)
    )

@app.get("/batch/status/{job_id}", response_model=BatchResultResponse)
async def get_batch_status(job_id: str):
    """
    Check status of batch job
    """
    if job_id not in job_store:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = job_store[job_id]
    
    return BatchResultResponse(
        job_id=job_id,
        status=job['status'],
        predictions=job.get('predictions'),
        completed_at=job.get('completed_at'),
        error=job.get('error')
    )

@app.get("/batch/result/{job_id}")
async def get_batch_result(job_id: str):
    """
    Retrieve completed batch results
    """
    if job_id not in job_store:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = job_store[job_id]
    
    if job['status'] != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Job status is {job['status']}, not completed"
        )
    
    return {
        "job_id": job_id,
        "predictions": job['predictions'],
        "total_samples": job['total_samples'],
        "completed_at": job['completed_at']
    }

# To test:
# curl -X POST "http://localhost:8000/batch/predict" -H "Content-Type: application/json" \
#   -d '{"data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]}'
# Then use returned job_id to check status:
# curl "http://localhost:8000/batch/status/{job_id}"
