"""
### Q6

**Question:** Create a function that returns a dictionary with counts of each unique element in a list.

**Input:** `['apple', 'orange', 'apple', 'banana']`

**Expected Output:** `{'apple': 2, 'orange': 1, 'banana': 1}`

**Usage:** Summarizing categorical survey results; counting different mutation types in a sequence; analyzing species distribution
"""

from collections import Counter

def count_unique_elements(lst):
    """
    Return frequency dictionary of unique elements.
    """
    return dict(Counter(lst))

# Test
result = count_unique_elements(['apple', 'orange', 'apple', 'banana'])
print(f"Element counts: {result}")  # Output: {'apple': 2, 'orange': 1, 'banana': 1}
