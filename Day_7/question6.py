"""
### Q6

**Question:** Create a function that returns the intersection of two dictionaries based on keys (returns a new dict with common keys and their values).

**Input:** `d1={'A':1, 'B':2, 'C':3}`, `d2={'B':4, 'C':5, 'D':6}`

**Expected Output:** `{'B': 2, 'C': 3}`

**Usage:** Merging overlapping gene annotations; finding common clinical variables between datasets; synchronizing shared model parameters
"""

def dict_key_intersection(d1, d2):
    """
    Return new dict with common keys from both dictionaries.
    Values come from d1 (first dict).
    """
    common_keys = set(d1.keys()) & set(d2.keys())
    return {key: d1[key] for key in common_keys}

# Test
d1 = {'A':1, 'B':2, 'C':3}
d2 = {'B':4, 'C':5, 'D':6}
result = dict_key_intersection(d1, d2)
print(f"Key intersection: {result}")  # Output: {'B': 2, 'C': 3}
