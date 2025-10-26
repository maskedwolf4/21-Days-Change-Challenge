"""
### Q4

**Question:** Create a function that performs random undersampling on the majority class to balance a binary classification dataset.

**Input:** `data=[(1,"A"), (1,"B"), (1,"C"), (1,"D"), (0,"E"), (0,"F")], seed=42`

**Expected Output:** `[(1,"A"), (1,"C"), (0,"E"), (0,"F")]` (balanced 2:2 ratio)

**Usage:** Handling class imbalance in fraud detection, balancing disease vs healthy samples, improving rare event prediction
"""
import random

def random_undersampling(data, seed=42):
    """
    Balance dataset by undersampling the majority class.
    """
    random.seed(seed)
    
    # Separate by class
    class_0 = [item for item in data if item[0] == 0]
    class_1 = [item for item in data if item[0] == 1]
    
    # Identify minority class size
    min_size = min(len(class_0), len(class_1))
    
    # Undersample majority class
    if len(class_0) > min_size:
        class_0 = random.sample(class_0, min_size)
    if len(class_1) > min_size:
        class_1 = random.sample(class_1, min_size)
    
    # Combine and shuffle
    balanced_data = class_0 + class_1
    random.shuffle(balanced_data)
    
    return balanced_data

# Test
result = random_undersampling([(1,"A"), (1,"B"), (1,"C"), (1,"D"), (0,"E"), (0,"F")], seed=42)
print(result)
