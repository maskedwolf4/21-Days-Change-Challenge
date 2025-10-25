"""
### Q4
**Question:** Create a function that generates bootstrapped samples (random sampling with replacement) from a dataset.

**Input:** `data=[10][20][30][40], n_samples=4, seed=42`

**Expected Output:** `[30][10][30][20]` (example with replacement)

**Usage:** Estimating confidence intervals in clinical studies, random forest algorithms, assessing model stability
"""

import random
def random_sampling(data: list, n_samples: int, seed: int) -> list:
    """A function that generates bootstrapped samples (random sampling with replacement) from a dataset."""

    random.seed(seed)

    shuffled_data = random.sample(data,n_samples)

    return shuffled_data

out_put = random_sampling(data=[10,20,30,40], n_samples=4, seed=42)
print(out_put) # [10, 40, 20, 30]

# import random

# def bootstrap_sample(data, n_samples, seed=None):
#     if seed is not None:
#         random.seed(seed)
#     return [random.choice(data) for _ in range(n_samples)]

# # Test
# data = [10, 20, 30, 40]
# print(bootstrap_sample(data, 4, seed=42))  # Output: [30, 10, 30, 20]
