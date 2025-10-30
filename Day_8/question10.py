"""
### Q10

**Question:** Implement a function to generate synthetic time series data using an autoregressive AR(1) model: x_t = φ * x_(t-1) + noise.

**Input:** `n_points=10, phi=0.7, initial_value=1.0, noise_std=0.1, seed=42`

**Expected Output:** `[1.0, 0.75, 0.61, 0.48, ...]` (10 values)

**Usage:** Simulating patient vital signs trajectories; generating synthetic biomarker data for testing algorithms; modeling temporal dependencies in biological processes
"""

import numpy as np

def generate_ar1_series(n_points, phi, initial_value, noise_std, seed=42):
    """
    Generate AR(1) time series: x_t = φ * x_(t-1) + ε_t
    where ε_t ~ N(0, noise_std²)
    """
    np.random.seed(seed)
    
    series = [initial_value]
    
    for _ in range(n_points - 1):
        noise = np.random.normal(0, noise_std)
        next_value = phi * series[-1] + noise
        series.append(next_value)
    
    return [round(x, 2) for x in series]

# Test
result = generate_ar1_series(10, 0.7, 1.0, 0.1, seed=42)
print(f"AR(1) series: {result}")
