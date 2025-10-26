"""
### Q6

**Question:** Create a function that performs label encoding by mapping categorical text labels to integer indices starting from 0.

**Input:** `["dog", "cat", "dog", "bird", "cat", "bird"]`

**Expected Output:** `[^1][^2][^1][^0][^2][^0]` with mapping `{"bird": 0, "cat": 2, "dog": 1}`

**Usage:** Encoding categorical variables for tree-based models, converting diagnosis codes to numerical format, preparing ordinal data
"""

def label_encoding(labels):
    """
    Encode categorical labels as integers.
    """
    # Create mapping from unique labels (sorted for consistency)
    unique_labels = sorted(set(labels))
    label_to_index = {label: idx for idx, label in enumerate(unique_labels)}
    
    # Encode the labels
    encoded = [label_to_index[label] for label in labels]
    
    return encoded, label_to_index

# Test
labels = ["dog", "cat", "dog", "bird", "cat", "bird"]
encoded, mapping = label_encoding(labels)
print(f"Encoded: {encoded}")
print(f"Mapping: {mapping}")
