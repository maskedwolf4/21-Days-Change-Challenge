"""
### Q9

**Question:** Create a function that performs string matching using the Knuth-Morris-Pratt (KMP) algorithm to find all occurrences of a pattern in text.

**Input:** `text="ABABDABACDABABCABAB"`, `pattern="ABABCABAB"`

**Expected Output:** `[14]`

**Usage:** Pattern matching in genomic sequences; finding regulatory motifs; text mining in biomedical literature
"""

def compute_lps(pattern):
    """Compute Longest Proper Prefix which is also Suffix (LPS) array for KMP."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Find all occurrences of pattern in text using KMP algorithm.
    Returns list of starting indices.
    """
    if not pattern or not text:
        return []
    
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    
    i = 0  # index for text
    j = 0  # index for pattern
    indices = []
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            indices.append(i - j)  # Found occurrence
            j = lps[j - 1]  # Continue for overlaps
        
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return indices

# Test
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = kmp_search(text, pattern)
print(f"Pattern occurrences at: {result}")  # Output: [14]
