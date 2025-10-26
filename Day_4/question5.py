"""
### Q5

**Question:** Write a function to calculate the interquartile range (IQR) which is the difference between the 75th and 25th percentiles.

**Input:** `[^1][^3][^5][^7][^9][^11][^13][^15][^17][^19]`

**Expected Output:** `10.0`

**Usage:** Detecting outliers in laboratory measurements, assessing data spread in clinical trials, robust statistical analysis
"""

import numpy as np

def calculate_iqr(data):
    """
    Calculate Interquartile Range (IQR).
    IQR = Q3 - Q1 (75th percentile - 25th percentile)
    """
    data = np.array(data)
    
    # Calculate quartiles
    q1 = np.percentile(data, 25)  # 25th percentile
    q3 = np.percentile(data, 75)  # 75th percentile
    
    # Calculate IQR
    iqr = q3 - q1
    
    return float(iqr)

# Test
result = calculate_iqr([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
print(f"IQR: {result}")  # Output: 10.0
