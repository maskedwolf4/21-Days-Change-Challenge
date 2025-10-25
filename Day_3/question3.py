"""
### Q3
**Question:** Write a function to calculate the Euclidean distance between two points in n-dimensional space.

**Input:** `point1=[1][2][3], point2=[4][6][8]`

**Expected Output:** `7.071`

**Usage:** Measuring similarity in feature space, k-nearest neighbors classification, clustering algorithms in patient stratification
"""

import math

def euclidean_distance(v1: list, v2: list) -> float:
    """A function to calculate the Euclidean distance between two points in n-dimensional space."""

    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

v1 = [1.0, 2.0, 3.0]
v2 = [4.0, 6.0, 8.0]
print(euclidean_distance(v1,v2))