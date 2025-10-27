
"""
### Q7

**Question:** Write a function to merge two dictionaries where values are lists and concatenate lists if the same key appears in both.

**Input:** `dict1={"A":[1][2], "B":[3]}, dict2={"A":[4], "C":[5][6]}`

**Expected Output:** `{"A": [1][2][4], "B":[3], "C":[5][6]}`

**Usage:** Integrating multi-source patient records; merging gene annotations; aggregating experimental replicates
"""


def merge_dicts(d1, d2):
    merged = d1.copy()
    for k, v in d2.items():
        if k in merged:
            merged[k] += v
        else:
            merged[k] = v.copy()
    return merged
