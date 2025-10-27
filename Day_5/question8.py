"""
### Q8

**Question:** Implement a function that removes outlier points from a data list using median absolute deviation (MAD) threshold of 3.

**Input:** `[2][3][4][100][5][3]`

**Expected Output:** `[2][3][4][5][3]`

**Usage:** Robust preprocessing in clinical lab measurements; filtering artifacts in brain imaging; outlier removal in financial time series
"""

import numpy as np

def remove_outliers(data, threshold=3):
    
    median = np.median(data)
    
    deviations = np.abs(data - median)
    
    mad = np.median(deviations)
    
    lower_bound = median - threshold * mad
    upper_bound = median + threshold * mad
    
    filtered_data = data[(data >= lower_bound) & (data <= upper_bound)]
    
    return filtered_data

#
data = np.array([1, 2, 3, 4, 5, 100])  # 100 is an outlier
cleaned_data = remove_outliers(data)
print("Cleaned Data without Outliers:", cleaned_data)





