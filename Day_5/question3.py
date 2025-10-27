"""
### Q3

**Question:** Write a function to compute the Manhattan distance between two coordinate points in n-dimensional space.

**Input:** `point1=[1][2][3], point2=[4][6][8]`

**Expected Output:** `12`

**Usage:** Clustering in high-dimensional data; comparing patient profiles in multi-omics analyses; analyzing spatial patterns in epidemiology
"""

def manhattan_distance(a, b):
    
    md = sum(abs(x - y) for x, y in zip(a, b))
    
    return md



        

    
