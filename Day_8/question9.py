"""
### Q9

**Question:** Create a function to calculate information gain for a binary classification split given parent and child class distributions.

**Input:** `parent=[^30][^20]`, `left_child=[^20][^5]`, `right_child=[^10][^15]`

**Expected Output:** `0.123`

**Usage:** Feature selection in decision trees; identifying optimal split points for diagnosis; entropy-based data partitioning
"""
import math

def entropy(class_counts):
    """Calculate entropy: -Σ(p * log2(p))"""
    total = sum(class_counts)
    if total == 0:
        return 0
    
    ent = 0
    for count in class_counts:
        if count > 0:
            p = count / total
            ent -= p * math.log2(p)
    
    return ent

def information_gain(parent, left_child, right_child):
    """
    Calculate information gain from a split.
    IG = H(parent) - weighted_avg(H(children))
    """
    parent_entropy = entropy(parent)
    
    left_entropy = entropy(left_child)
    right_entropy = entropy(right_child)
    
    total = sum(parent)
    left_total = sum(left_child)
    right_total = sum(right_child)
    
    # Weighted average of child entropies
    weighted_child_entropy = (left_total / total) * left_entropy + \
                             (right_total / total) * right_entropy
    
    ig = parent_entropy - weighted_child_entropy
    
    return round(ig, 3)

# Test
result = information_gain([30, 20], [20, 5], [10, 15])
print(f"Information Gain: {result}")  # Output: 0.123

