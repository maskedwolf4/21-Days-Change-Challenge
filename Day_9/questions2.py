"""

**Q2: Feature Normalization Calculator**
Question: Create a function that normalizes a list of numerical features using Min-Max scaling (scale to 0-1 range).

Input: `[^10][^20][^30][^40][^50]`

Expected Output: `[0.0, 0.25, 0.5, 0.75, 1.0]`

Usage: Essential preprocessing step in neural networks and gradient descent-based algorithms to ensure all features contribute equally.[^7]
"""

def min_max_scaler(data: list) -> list:

    n_max = max(data)
    n_min = min(data)

    den = n_max - n_min

    scaled_data = ((x - n_min)/den for x in data)
    scaled_data = list(scaled_data)

    return scaled_data

print(min_max_scaler([10,20,30,40,50]))