"""
### Q3

**Question:** Write a function to perform element-wise multiplication of two lists of equal length.

**Input:** `[^2][^4][^6]`, `[^1][^3][^5]`

**Expected Output:** `[^2][^12][^30]`

**Usage:** Combining arrays of coefficients and features; simulating signal processing pipelines; calculating weighted scores in ensemble models
"""

def element_wise_multiply(lst1, lst2):
    """
    Multiply corresponding elements of two lists.
    Assumes lists are of equal length.
    """
    if len(lst1) != len(lst2):
        raise ValueError("Lists must be of equal length")
    
    return [a * b for a, b in zip(lst1, lst2)]

# Test
result = element_wise_multiply([2, 4, 6], [1, 3, 5])
print(f"Element-wise product: {result}")  # Output: [2, 12, 30]
