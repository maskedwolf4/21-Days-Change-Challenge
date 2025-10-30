"""
### Q6

**Question:** Create a function that removes duplicate elements from a list while preserving the original order.

**Input:** `[^3][^5][^3][^2][^5][^7][^2][^9]`

**Expected Output:** `[^3][^5][^2][^7][^9]`

**Usage:** Deduplicating patient IDs in merged datasets; removing redundant features in ML pipelines; cleaning repeated entries in biological databases
"""

def remove_diplicate(data: list) -> list:
    """A unction that removes duplicate elements from a list while preserving the original order."""

    order_data = dict.fromkeys(data)
    order_data = list(order_data.keys())



    return order_data

print(remove_diplicate([3,5,3,2,5,7,2,9]))
