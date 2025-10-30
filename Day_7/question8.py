"""
### Q8

**Question:** Write a function to compute the weighted average of a list of numbers with corresponding weights.

**Input:** `values=[10][20][30][40]`, `weights=[0.1, 0.2, 0.3, 0.4]`

**Expected Output:** `25.0`

**Usage:** Calculating weighted gene expression scores; importance-based feature aggregation; risk-adjusted clinical scoring systems
"""

def weighted_average(values, weights):
    """
    Compute weighted average: Σ(value_i * weight_i) / Σ(weight_i)
    """
    if len(values) != len(weights) or not values:
        return None
    
    total_weighted = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)
    
    return total_weighted / total_weight if total_weight != 0 else None

# Test
result = weighted_average([10, 20, 30, 40], [0.1, 0.2, 0.3, 0.4])
print(f"Weighted average: {result}")  # Output: 25.0
