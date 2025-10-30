"""
### Q1

**Question:** Write a function to calculate the standard error of the mean (SEM) for a list of numbers using the formula: SEM = std / √n.

**Input:** `[^12][^15][^14][^10][^13][^11]`

**Expected Output:** `0.764`

**Usage:** Estimating uncertainty in sample means for clinical trials; calculating error bars for gene expression plots; statistical inference in experimental biology
"""

from statistics import stdev
from math import pow

def sem(data: list) -> float:
    """A function to calculate standard error of the menan"""

    std = stdev(data=data)

    n = len(data)

    d = pow(n,1/2)

    sem = std/d

    sem = round(sem,3)

    return sem

print(sem([12,15,14,10,13,11]))