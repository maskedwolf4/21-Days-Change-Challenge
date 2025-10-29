"""
**Question:** Write a function to compute the Dice coefficient (similarity) between two sets.

**Input:** `set1={"gene1","gene2","gene3"}, set2={"gene2","gene4","gene5"}`

**Expected Output:** `0.333`

**Usage:** Comparing sample overlaps in cohort selection; quantifying annotation similarity; feature selection in omics data
"""

def dice_coefficient(set1, set2):
    """
    Calculate Dice similarity coefficient.
    Formula: 2 * |A ∩ B| / (|A| + |B|)
    """
    intersection = len(set1 & set2)
    union_size = len(set1 | set2)
    
    if union_size == 0:
        return 1.0  # Edge case: both empty
    
    return round(2 * intersection / union_size, 3)

# Test
set1 = {"gene1", "gene2", "gene3"}
set2 = {"gene2", "gene4", "gene5"}
result = dice_coefficient(set1, set2)
print(f"Dice coefficient: {result}")  # Output: 0.333
