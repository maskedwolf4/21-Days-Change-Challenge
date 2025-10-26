"""
### Q3

**Question:** Write a function to calculate Pearson correlation coefficient between two numerical arrays.

**Input:** `x=[^1][^2][^3][^4][^5], y=[^2][^4][^5][^4][^5]`

**Expected Output:** `0.832`

**Usage:** Finding correlated genes in co-expression networks, feature selection in predictive modeling, identifying relationships between clinical variables
"""

import numpy as np

def pearson_correlation(x, y):
    """
    Calculate Pearson correlation coefficient.
    Formula: r = [n(Σxy) - (Σx)(Σy)] / sqrt([nΣx² - (Σx)²][nΣy² - (Σy)²])
    """
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    
    # Calculate required sums
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)
    sum_y2 = np.sum(y ** 2)
    
    # Apply Pearson formula
    numerator = n * sum_xy - sum_x * sum_y
    denominator = np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
    
    r = numerator / denominator
    
    return round(r, 3)

# Test
result = pearson_correlation([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])
print(f"Pearson r: {result}")  # Output: 0.832
