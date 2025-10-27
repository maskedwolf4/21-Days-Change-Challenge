"""
### Q10

**Question:** Create a function that ranks items in a list in descending order and returns a dictionary mapping the item to its rank (starting from 1).

**Input:** `[56][42][85][16]`

**Expected Output:** `{85: 1, 56: 2, 42: 3, 16: 4}`

**Usage:** Scoring models in competitions; ranking biomarkers by predictive value; prioritizing candidate genes in genome-wide studies
"""

def rank_descending(lst):
    sorted_lst = sorted(lst, reverse=True)
    return {v: i+1 for i, v in enumerate(sorted_lst)}
