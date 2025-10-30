"""
### Q7

**Question:** Implement a function to find the median of a list of numbers (handle both odd and even length lists correctly).

**Input:** `[7][3][1][4][6]`

**Expected Output:** `4`

**Usage:** Robust central tendency measure in biomedical statistics; outlier-resistant analysis of lab measurements; non-parametric data analysis
"""

def calculate_median(numbers):
    """
    Calculate median: middle value for odd length, average of two middle for even.
    """
    if not numbers:
        return None
    
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    if n % 2 == 1:
        # Odd length: middle element
        return sorted_nums[n // 2]
    else:
        # Even length: average of two middle elements
        mid1 = sorted_nums[n // 2 - 1]
        mid2 = sorted_nums[n // 2]
        return (mid1 + mid2) / 2

# Test
result = calculate_median([7, 3, 1, 4, 6])
print(f"Median: {result}")  # Output: 4
