"""
**Question:** Implement a function to calculate the Spearman rank correlation coefficient between two numeric lists (convert to ranks first, then calculate Pearson on ranks).

**Input:** `x=[^1][^2][^3][^4][^5]`, `y=[^5][^6][^7][^8][^7]`

**Expected Output:** `0.82`

**Usage:** Non-parametric correlation for ordinal clinical data; robust correlation for non-linear relationships; analyzing ranked gene expression patterns
"""
from math import pow
# from scipy.stats import rankdata # type: ignore

def spearman_rank_correlation_coefficient(xlist: list, ylist: list) -> float:

    n = len(xlist)+len(ylist)

    
    xranks = [sorted(xlist).index(x) for x in xlist]
    xranks = [x+1 for x in xranks ]
    yranks = [sorted(ylist).index(y) for y in ylist]
    yranks = [y+1 for y in yranks ]

    # alternate stratergy for ranking data
    # xranks = rankdata(xlist)
    # yranks = rankdata(ylist)



    diff = [a - b for a, b in zip(xranks, yranks)]

    num = sum(pow(a,2)for a in diff)*6
    den = n*(pow(n,2)-1)

    p = 1-(num/den)

    return p
print(spearman_rank_correlation_coefficient(xlist=[1,2,3,4,5],ylist=[5,6,7,8,9]))
