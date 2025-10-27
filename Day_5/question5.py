"""
### Q5

**Question:** Write a function to compute the geometric mean of a list of positive numbers.

**Input:** `[1][3][9][27]`

**Expected Output:** `6.0`

**Usage:** Calculating average growth rates; aggregating gene expression fold changes; analyzing cell proliferation data
"""
from math import prod, pow

def geometric_mean(points: list) -> float:
    """A function to compute the geometric mean of a list of positive numbers."""

    n = len(points)

    pro = prod(points)

    gm = pow(pro,1/n)

    return gm

print(geometric_mean([1,3,9,27]))