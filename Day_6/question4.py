"""
### Q4

**Question:** Create a function to return the cumulative sum list of a given numeric list.

**Input:** `[^4][^2][^5][^3]`

**Expected Output:** `[^4][^6][^11][^14]`

**Usage:** Generating running totals in time-series; measuring cumulative population or resource growth; financial data analysis
"""

def cumulative_sum(lst):
    """
    Calculate running total of elements in the list.
    Each element is the sum of all previous elements including itself.
    """
    if not lst:
        return []
    
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    
    return result

# Test
result = cumulative_sum([4, 2, 5, 3])
print(f"Cumulative sum: {result}")  # Output: [4, 6, 11, 14]
