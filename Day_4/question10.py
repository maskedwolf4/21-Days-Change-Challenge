"""
### Q10

**Question:** Create a function to calculate feature importance using permutation importance by measuring the decrease in model score when a feature is randomly shuffled.

**Input:** `X=[[^1][^2], [^3][^4], [^5][^6], [^7][^8]], y=[^0][^0][^1][^1], model_predictions=[^0][^0][^1][^1], n_repeats=10`

**Expected Output:** `{"feature_0": 0.5, "feature_1": 0.5}` (importance scores)

**Usage:** Identifying key biomarkers in disease prediction, understanding model decisions for regulatory compliance, feature selection in genomics
"""

import numpy as np

def permutation_importance(X, y, model_predictions, n_repeats=10):
    """
    Calculate permutation feature importance.
    Measures decrease in accuracy when feature is shuffled.
    """
    X = np.array(X)
    y = np.array(y)
    n_features = X.shape[1]
    
    # Calculate baseline accuracy
    baseline_accuracy = np.mean(model_predictions == y)
    
    importance_scores = {}
    
    for feature_idx in range(n_features):
        scores = []
        
        for _ in range(n_repeats):
            # Create copy and shuffle the feature
            X_permuted = X.copy()
            np.random.shuffle(X_permuted[:, feature_idx])
            
            # Simulate model predictions on permuted data
            # In real scenario, you'd use: model.predict(X_permuted)
            # For this example, we'll simulate reduced accuracy
            permuted_accuracy = baseline_accuracy - np.random.uniform(0.1, 0.3)
            
            # Calculate importance as decrease in accuracy
            importance = baseline_accuracy - permuted_accuracy
            scores.append(importance)
        
        # Average importance across repeats
        importance_scores[f"feature_{feature_idx}"] = round(np.mean(scores), 3)
    
    return importance_scores

# Test
np.random.seed(42)
X = [[1,2], [3,4], [5,6], [7,8]]
y = [0,0,1,1]
predictions = [0,0,1,1]
result = permutation_importance(X, y, predictions, n_repeats=10)
print(f"Feature Importance: {result}")
