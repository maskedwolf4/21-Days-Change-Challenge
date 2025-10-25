"""
### Q7
**Question:** Implement the Levenshtein distance (edit distance) calculation between two strings using dynamic programming to find minimum insertions, deletions, and substitutions.

**Input:** `string1="KITTEN", string2="SITTING"`

**Expected Output:** `3`

**Usage:** Spell checking in biomedical literature mining, measuring mutation distance between sequences, fuzzy matching in database searches
"""

def levenshtein_distance(string1, string2):
    m, n = len(string1), len(string2)
    
    # Create DP matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i-1] == string2[j-1]:
                cost = 0
            else:
                cost = 1
            
            dp[i][j] = min(
                dp[i-1][j] + 1,      # deletion
                dp[i][j-1] + 1,      # insertion
                dp[i-1][j-1] + cost  # substitution
            )
    
    return dp[m][n]

# Test
print(levenshtein_distance("KITTEN", "SITTING"))  # Output: 3
