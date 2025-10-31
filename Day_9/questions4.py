"""
**Q4: Batch Data Generator**
Question: Create a function that splits a dataset (list) into batches of specified size. The last batch can be smaller if data doesn't divide evenly.

Input: `data=[^1][^2][^3][^4][^5][^6][^7][^8][^9], batch_size=4`

Expected Output: `[[^1][^2][^3][^4], [^5][^6][^7][^8], [^9]]`

Usage: Critical for training deep learning models with mini-batch gradient descent to manage memory efficiently with large datasets.
"""

def split_dataset(data: list, batch_size: int) -> list:
    """A function that splits a dataset (list) into batches of specified size."""

    splitted_data = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

    return splitted_data

print(split_dataset([1,2,3,4,5,6,7,8,9],4))

    

