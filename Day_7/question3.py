"""
## Q3

**Question:** Write a function to rotate a list left by k positions (move first k elements to the end).

**Input:** `lst=[1][2][3][4][5][6]`, `k=2`

**Expected Output:** `[3][4][5][6][1][2]`

**Usage:** Circular buffer management for streaming sensor data; cyclic shift operations in signal processing; DNA circular genome analysis
"""

def left_rotate(lst, k):
    """
    Rotate list left by k positions.
    Equivalent to lst[k:] + lst[:k]
    """
    if not lst:
        return lst
    
    k = k % len(lst)  # Handle k >= len(lst)
    return lst[k:] + lst[:k]

# Test
result = left_rotate([1, 2, 3, 4, 5, 6], 2)
print(f"Left rotated: {result}")  # Output: [3, 4, 5, 6, 1, 2]


