"""
### Q8

**Question:** Write a function to perform stratified k-fold split indices for a dataset given labels (return list of k train-test index tuples).

**Input:** `labels=[^0][^0][^0][^0][^1][^1][^1][^1], k=2`

**Expected Output:** `[([^0][^1][^4][^5], [^2][^3][^6][^7]), ([^2][^3][^6][^7], [^0])]` (approximate, maintaining class balance)

**Usage:** Cross-validation for imbalanced disease datasets; fair evaluation of diagnostic classifiers; training robust predictive models
"""

import numpy as np

def stratified_k_fold_indices(labels, k):
    """
    Generate stratified k-fold split indices maintaining class balance.
    Returns list of (train_indices, test_indices) tuples.
    """
    labels = np.array(labels)
    n_samples = len(labels)
    
    # Separate indices by class
    class_indices = {}
    for label in np.unique(labels):
        class_indices[label] = np.where(labels == label)[0]
    
    folds = []
    
    # Create k folds
    for fold_idx in range(k):
        test_indices = []
        train_indices = []
        
        for label, indices in class_indices.items():
            # Shuffle indices for randomness
            np.random.shuffle(indices)
            
            # Calculate fold size for this class
            fold_size = len(indices) // k
            start = fold_idx * fold_size
            end = start + fold_size if fold_idx < k - 1 else len(indices)
            
            # Assign to test and train
            test_indices.extend(indices[start:end])
            train_indices.extend(np.concatenate([indices[:start], indices[end:]]))
        
        folds.append((sorted(train_indices), sorted(test_indices)))
    
    return folds

# Test
np.random.seed(42)
result = stratified_k_fold_indices([0,0,0,0,1,1,1,1], k=2)
print(f"Stratified folds: {result}")
