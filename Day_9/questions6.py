"""
**Q6: Train-Test Split Function**
Question: Create a function that randomly splits a dataset into training and testing sets based on a given ratio (e.g., 80-20 split). Use a seed for reproducibility.

Input: `data=[^1][^2][^3][^4][^5][^6][^7][^8][^9][^10], train_ratio=0.8, seed=42`

Expected Output: `{'train': [^1][^3][^4][^6][^7][^8][^9][^10], 'test': [^2][^5]}`

Usage: Fundamental for evaluating machine learning model performance and preventing overfitting by testing on unseen data.
"""

import random

def train_test_split(data: list, train_ratio: float, seed: int) -> dict:


    random.seed(seed)
    random.shuffle(data)

    n = (train_ratio*100)/10

    n = int(n)

    if n == 0:
        n = train_ratio*100
        n = int(n)

    train = data[:n]
    test = data[n:]

    train_and_test_data = {"train": train, "test": test}

    return train_and_test_data

print(train_test_split(data=[1,2,3,4,5,6,7,8,9,10],train_ratio=0.8,seed=42)) # output: {'train': [8, 4, 3, 9, 6, 7, 10, 5], 'test': [1, 2]}



