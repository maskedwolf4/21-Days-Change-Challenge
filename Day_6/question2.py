"""
### Q2

**Question:** Create a function that returns the indices of all local maxima in a numeric list.

**Input:** `[^1][^3][^7][^1][^2][^6][^0][^1]`

**Expected Output:** `[^2][^5]`

**Usage:** Detecting peaks in sensor signals; finding gene expression spikes; identifying events in physiological time series
"""

def find_local_maxima(lst):
    """
    Find indices where values are greater than their immediate neighbors.
    Edge cases: first and last elements can't be local maxima.
    """
    if len(lst) < 3:
        return []
    
    maxima_indices = []
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            maxima_indices.append(i)
    
    return maxima_indices

# Test
result = find_local_maxima([1, 3, 7, 1, 2, 6, 0, 1])
print(f"Local maxima indices: {result}")  # Output: [2, 5]
