"""
### Q5
**Question:** Write a function to calculate the coefficient of variation (CV) which is standard deviation divided by mean, expressed as percentage.

**Input:** `[2.1, 2.3, 2.2, 2.4, 2.0]`

**Expected Output:** `6.93`

**Usage:** Quality control in qPCR experiments, comparing variability across different scales, assessing technical reproducibility
"""
from math import sqrt
def coefficient_variation(data: list) -> float:
    """A function to calculate the coefficient of variation (CV) which is standard deviation divided by mean, expressed as percentage."""

    mean = sum(data) / len(data)

    var = sum((a-mean)**2 for a in data)/ (len(data)-1)

    sd = sqrt(var)

    cv = sd/mean *100

    return cv

cv = coefficient_variation([2.1, 2.3, 2.2, 2.4, 2.0])
print(cv)

