"""
### Q4

**Question:** Create a function to count the number of missing (NaN) values in a dataset list.

**Input:** `[1.2, np.nan, 5.6, np.nan, 3.4, 2.1]`

**Expected Output:** `2`

**Usage:** Data cleaning in biomedical research; handling sensor dropouts; preparing health survey data for machine learning
"""

import numpy as np

def count_nan(df: list) -> int:
    """A function to count the number of missing (NaN) values in a dataset list."""

    nan_count = df.count(np.nan)

    return nan_count

print(count_nan([1.2, np.nan, 5.6, np.nan, 3.4, 2.1]))
