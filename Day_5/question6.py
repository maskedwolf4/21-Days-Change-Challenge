"""
**Question:** Create a function to flatten a nested list of arbitrary depth.

**Input:** `[[1, [2, [3][4]], 5]]`

**Expected Output:** `[1][2][3][4][5]`

**Usage:** Normalizing hierarchical biological data; flattening outputs from recursive simulations; preprocessing tree-like data structures
"""

def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat
