"""
### Q4

**Question:** Create a function to calculate the variance of a list of numbers using the formula: variance = Σ(x - mean)² / n.

**Input:** `[^2][^4][^4][^4][^5][^5][^7][^9]`

**Expected Output:** `4.0`

**Usage:** Measuring spread in phenotypic measurements; assessing variability in sensor readings; quality control in laboratory assays
"""
from math import pow

def variance(data:list) -> float:
    """A function to calculate variance"""

    n =len(data)

    mean = sum(data)/n

    numerator = sum(pow(x-mean,2) for x in data)

    var = numerator/n

    return var

data = [2,4,4,4,5,5,7,9]

print(variance(data=data))


    