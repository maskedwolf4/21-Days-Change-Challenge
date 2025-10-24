"""
### Q10

**Question:** Write a function using NumPy to calculate the pairwise Euclidean distance matrix between all rows of a 2D array efficiently without loops.

**Input:** `np.array([[1][2], [3][4], [5][6]])`

**Expected Output:** 3x3 symmetric matrix with distances between each pair of points

**Usage:** K-means clustering initialization and nearest neighbor searches in ML pipelines.
"""

import numpy as np

def pairwise_euclidean_distance(X):
    """Calculate pairwise Euclidean distances without loops"""
    # Using broadcasting: sqrt(sum((a - b)^2))
    # Expand: ||a-b||^2 = ||a||^2 + ||b||^2 - 2*a·b
    
    sum_sq = np.sum(X**2, axis=1)
    distances = np.sqrt(
        sum_sq[:, np.newaxis] + sum_sq[np.newaxis, :] - 2 * np.dot(X, X.T)
    )
    return distances

# Usage
X = np.array([[1, 2], [3, 4], [5, 6]])
dist_matrix = pairwise_euclidean_distance(X)
print(dist_matrix)
