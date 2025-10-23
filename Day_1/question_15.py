"""
**Q15 - Pydantic Model for ML Experiment Tracking**
Question: Create nested Pydantic models for ML experiment configuration (model params, dataset info, training config) with validation rules.
Input: Dictionary with experiment parameters
Expected Output: Validated ExperimentConfig object
Usage: Configuration management in MLOps and experiment tracking systems
"""
from pydantic import BaseModel, Field, validator
from typing import Dict, List, Optional
from datetime import datetime
from enum import Enum

class ModelType(str, Enum):
    CNN = "cnn"
    RNN = "rnn"
    TRANSFORMER = "transformer"
    RANDOM_FOREST = "random_forest"

class DatasetConfig(BaseModel):
    name: str
    train_size: int = Field(..., gt=0)
    val_size: int = Field(..., gt=0)
    test_size: int = Field(..., gt=0)
    features: List[str]
    target: str
    
    @validator('val_size', 'test_size')
    def validate_split_size(cls, v, values):
        if 'train_size' in values and v > values['train_size']:
            raise ValueError('Validation/test size cannot exceed training size')
        return v

class ModelParams(BaseModel):
    model_type: ModelType
    learning_rate: float = Field(..., gt=0, le=1)
    batch_size: int = Field(..., gt=0)
    epochs: int = Field(..., gt=0, le=1000)
    hidden_layers: Optional[List[int]] = None
    dropout_rate: Optional[float] = Field(None, ge=0, le=1)

class TrainingConfig(BaseModel):
    optimizer: str
    loss_function: str
    metrics: List[str]
    early_stopping: bool = True
    patience: int = Field(default=5, gt=0)

class ExperimentConfig(BaseModel):
    experiment_name: str
    experiment_id: str
    created_at: datetime = Field(default_factory=datetime.now)
    dataset: DatasetConfig
    model: ModelParams
    training: TrainingConfig
    random_seed: int = 42
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

# Test
config_dict = {
    "experiment_name": "sentiment_analysis_v1",
    "experiment_id": "exp_001",
    "dataset": {
        "name": "IMDB_reviews",
        "train_size": 20000,
        "val_size": 5000,
        "test_size": 5000,
        "features": ["text", "cleaned_text"],
        "target": "sentiment"
    },
    "model": {
        "model_type": "transformer",
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 50,
        "hidden_layers": [512, 256],
        "dropout_rate": 0.3
    },
    "training": {
        "optimizer": "adam",
        "loss_function": "binary_crossentropy",
        "metrics": ["accuracy", "f1_score"],
        "early_stopping": True,
        "patience": 10
    }
}

experiment = ExperimentConfig(**config_dict)
print(experiment.json(indent=2))
print(f"\nModel type: {experiment.model.model_type}")
print(f"Total dataset size: {experiment.dataset.train_size + experiment.dataset.val_size + experiment.dataset.test_size}")
