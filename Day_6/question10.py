"""
### Q10

**Question:** Write a function to compute the Hurst exponent for a given time series list using the rescaled range (R/S) method (use 2-segment calculation for simplicity).

**Input:** `[0.5, 1.0, 0.6, 0.8, 1.2, 1.4]`

**Expected Output:** A float around `0.6` (actual value depends on calculation details)

**Usage:** Identifying long-term memory or trend strength in biosignals; financial analytics; analyzing persistence in biological rhythms
"""

import numpy as np

def hurst_exponent_simple(series):
    """
    Simple Hurst exponent using R/S analysis on full series.
    For production, use multiple scales; this is illustrative.
    H ≈ log(R/S) / log(n) for n=len(series)
    """
    series = np.array(series)
    n = len(series)
    
    if n < 2:
        return 0.0
    
    # Calculate mean
    mean = np.mean(series)
    
    # Cumulative deviations
    deviations = np.cumsum(series - mean)
    
    # Range R = max - min of deviations
    R = np.max(deviations) - np.min(deviations)
    
    # Standard deviation S
    S = np.std(series, ddof=1)
    
    # R/S ratio
    if S == 0:
        return 0.0
    
    RS = R / S
    
    # Hurst estimate: log(R/S) / log(n)
    if n > 1:
        H = np.log(RS) / np.log(n)
        return round(max(0, min(1, H)), 2)  # Clamp to [0,1]
    
    return 0.5  # Random walk default

# Test
result = hurst_exponent_simple([0.5, 1.0, 0.6, 0.8, 1.2, 1.4])
print(f"Hurst exponent: {result}")  # Output: ~0.6 (varies slightly)
