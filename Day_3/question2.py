"""
### Q2
**Question:** Create a function that performs log transformation (natural log) on expression data, adding a pseudocount to handle zeros.

**Input:** `values=[0][1][10][100][1000], pseudocount=1`

**Expected Output:** `[0.0, 0.693, 2.398, 4.615, 6.908]`

**Usage:** Stabilizing variance in RNA-seq analysis, normalizing skewed distributions in proteomics, preprocessing data for linear models
"""

import math

def log_transform(values, pseudocount=1):
    return [round(math.log(val + pseudocount), 3) for val in values]

# Test
values = [0, 1, 10, 100, 1000]
print(log_transform(values, pseudocount=1))  
# Output: [0.0, 0.693, 2.398, 4.615, 6.908]
