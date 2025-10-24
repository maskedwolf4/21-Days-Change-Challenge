"""
**Question:** Build a FastAPI application with dependency injection for database connection pooling, implementing CRUD endpoints for managing experiment metadata with async database operations.

**Input:** `GET /experiments/{experiment_id}`

**Expected Output:** JSON response with experiment details or 404 if not found

**Usage:** Laboratory information management systems (LIMS) and research data management platforms.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
import asyncpg
from contextlib import asynccontextmanager

# Database connection pool
class Database:
    pool: Optional[asyncpg.Pool] = None

db = Database()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create connection pool
    db.pool = await asyncpg.create_pool(
        host='localhost',
        port=5432,
        user='user',
        password='password',
        database='lims_db',
        min_size=5,
        max_size=20
    )
    yield
    # Shutdown: Close pool
    await db.pool.close()

app = FastAPI(lifespan=lifespan)

# Pydantic models
class ExperimentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    experiment_type: str
    researcher: str

class ExperimentResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    experiment_type: str
    researcher: str
    created_at: str

# Dependency
async def get_db():
    async with db.pool.acquire() as connection:
        yield connection

@app.post("/experiments", response_model=ExperimentResponse, 
          status_code=status.HTTP_201_CREATED)
async def create_experiment(
    experiment: ExperimentCreate,
    conn = Depends(get_db)
):
    """Create new experiment record"""
    query = """
        INSERT INTO experiments (name, description, experiment_type, researcher)
        VALUES ($1, $2, $3, $4)
        RETURNING id, name, description, experiment_type, researcher, 
                  created_at::text
    """
    row = await conn.fetchrow(
        query,
        experiment.name,
        experiment.description,
        experiment.experiment_type,
        experiment.researcher
    )
    return dict(row)

@app.get("/experiments/{experiment_id}", response_model=ExperimentResponse)
async def get_experiment(experiment_id: int, conn = Depends(get_db)):
    """Retrieve experiment by ID"""
    query = """
        SELECT id, name, description, experiment_type, researcher, 
               created_at::text
        FROM experiments
        WHERE id = $1
    """
    row = await conn.fetchrow(query, experiment_id)
    
    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Experiment {experiment_id} not found"
        )
    
    return dict(row)

@app.get("/experiments", response_model=List[ExperimentResponse])
async def list_experiments(
    skip: int = 0,
    limit: int = 100,
    conn = Depends(get_db)
):
    """List all experiments with pagination"""
    query = """
        SELECT id, name, description, experiment_type, researcher, 
               created_at::text
        FROM experiments
        ORDER BY created_at DESC
        LIMIT $1 OFFSET $2
    """
    rows = await conn.fetch(query, limit, skip)
    return [dict(row) for row in rows]

@app.delete("/experiments/{experiment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_experiment(experiment_id: int, conn = Depends(get_db)):
    """Delete experiment by ID"""
    query = "DELETE FROM experiments WHERE id = $1 RETURNING id"
    row = await conn.fetchrow(query, experiment_id)
    
    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Experiment {experiment_id} not found"
        )

# Run with: uvicorn app:app --reload
