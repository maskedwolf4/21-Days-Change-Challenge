"""
### Q2

**Question:** Create a function to find the second largest element in a list without using sorting.

**Input:** `[^10][^20][^4][^45][^99][^99][^45]`

**Expected Output:** `45`

**Usage:** Finding runner-up biomarker scores; identifying secondary peaks in chromatography; rank-based feature selection in machine learning
"""

def second_largest(lst:list) -> int:
    """
    Find second largest unique element without sorting.
    Single pass O(n) algorithm.
    """
    if len(lst) < 2:
        return None
    
    largest = second = float('-inf')
    
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second if second != float('-inf') else None

# Test
result = second_largest([10, 20, 4, 45, 99, 99, 45])
print(f"Second largest: {result}")  # Output: 45



