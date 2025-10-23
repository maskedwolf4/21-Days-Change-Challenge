"""
**Q23 - ML Model Serving Endpoint**
Question: Create a FastAPI endpoint with Pydantic models that accepts feature vectors, runs inference using a loaded model, and returns predictions with confidence scores.
Input: POST request with feature array
Expected Output: JSON with prediction and confidence
Usage: Deploying machine learning models as REST APIs in production
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List
import numpy as np
import joblib
from datetime import datetime

app = FastAPI(title="ML Model Serving API")

class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_items=1)
    model_version: str = Field(default="v1.0")
    
    @validator('features')
    def validate_features(cls, v):
        if any(np.isnan(x) or np.isinf(x) for x in v):
            raise ValueError('Features contain NaN or Inf values')
        return v

class PredictionResponse(BaseModel):
    prediction: float
    confidence: float
    model_version: str
    timestamp: str

class ModelServer:
    """Manages model loading and inference"""
    
    def __init__(self):
        # Simulate loaded model (in production, use joblib.load())
        self.model = None
        self.model_version = "v1.0"
    
    def predict(self, features: np.ndarray):
        """
        Runs inference
        In production, this would call self.model.predict()
        """
        # Simulated prediction
        prediction = np.mean(features) * 2.5 + 10.0
        
        # Simulated confidence (would come from model.predict_proba())
        confidence = 0.85 + np.random.uniform(-0.1, 0.1)
        confidence = np.clip(confidence, 0, 1)
        
        return prediction, confidence

# Initialize model server
model_server = ModelServer()

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """
    Endpoint for model predictions
    """
    try:
        features_array = np.array(request.features).reshape(1, -1)
        
        prediction, confidence = model_server.predict(features_array)
        
        return PredictionResponse(
            prediction=float(prediction),
            confidence=float(confidence),
            model_version=model_server.model_version,
            timestamp=datetime.now().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_version": model_server.model_version,
        "timestamp": datetime.now().isoformat()
    }

# To run: uvicorn filename:app --reload
# Test with: curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"features": [1.5, 2.3, 4.1, 0.8]}'
