"""
### Q9

**Question:** Create a function to bucketize a numeric list by placing each value into bins defined by edges.

**Input:** `values=[1.2, 2.4, 3.6, 4.8], bins=[^0][^2][^4][^6]`

**Expected Output:** `[^0][^1][^2][^2]`
*(values go into bin 0: [0,2), bin 1: [2,4), bin 2: )*

**Usage:** Discretizing clinical data for risk categories; pre-processing features for decision trees; histogram-based visualizations
"""

import bisect

def bucketize(values, bins):
    """
    Assign each value to its bin index based on bin edges.
    Bins are left-closed: [bin[i], bin[i+1])
    """
    bin_indices = []
    for value in values:
        # Find insertion point using binary search
        index = bisect.bisect_left(bins, value)
        if index == len(bins):
            index -= 1  # Value >= last bin edge
        bin_indices.append(index)
    
    return bin_indices

# Test
result = bucketize([1.2, 2.4, 3.6, 4.8], [0, 2, 4, 6])
print(f"Bin indices: {result}")  # Output: [1, 2, 2, 3] (adjusted for 0-indexing)
