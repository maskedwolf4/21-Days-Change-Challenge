"""
### Q2

**Question:** Create a function that performs standard scaling (z-score standardization) on features by subtracting mean and dividing by standard deviation.

**Input:** `[^10][^12][^23][^23][^16][^23][^21][^16]`

**Expected Output:** `[-1.5, -1.125, 0.75, 0.75, -0.375, 0.75, 0.375, -0.375]`

**Usage:** Preprocessing features for support vector machines, standardizing metabolomics data, preparing inputs for gradient-based optimization
"""
import numpy as np

def standard_scaling(data):
    """
    Perform z-score normalization.
    Formula: z = (x - μ) / σ
    """
    data = np.array(data)
    
    # Calculate mean and standard deviation
    mean = np.mean(data)
    std = np.std(data, ddof=0)  # Population standard deviation
    
    # Apply z-score formula
    scaled_data = (data - mean) / std
    
    return scaled_data.tolist()

# Test
result = standard_scaling([10, 12, 23, 23, 16, 23, 21, 16])
print([round(x, 3) for x in result])
