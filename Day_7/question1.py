"""
### Q1

**Question:** Write a function to find the mode (most frequent value) in a numeric list. If there are multiple modes, return the first one encountered.

**Input:** `[3][7][3][5][3][9][1]`

**Expected Output:** `3`

**Usage:** Identifying predominant cell types in tissue samples; finding most common mutation variants; summarizing survey responses in clinical studies
"""

from collections import Counter

def find_mode(numbers):
    """
    Find the most frequent value (mode) in a list.
    Returns the first occurrence if multiple modes exist.
    """
    if not numbers:
        return None
    
    # Count frequency of each number
    frequency = Counter(numbers)
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find all numbers with max frequency
    candidates = [num for num, freq in frequency.items() if freq == max_freq]
    
    # Return the first one that appears in original order
    for num in numbers:
        if num in candidates:
            return num
    
    return candidates[0]  # Fallback

# Test
result = find_mode([3, 7, 3, 5, 3, 9, 1])
print(f"Mode: {result}")  # Output: 3
