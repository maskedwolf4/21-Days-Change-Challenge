"""
### Q8

**Question:** Implement a function that returns the longest common prefix among a list of DNA sequences.

**Input:** `["ATGCC", "ATGCACT", "ATGCTT"]`

**Expected Output:** `"ATGC"`

**Usage:** Multiple sequence alignment pre-processing; identifying conserved regulatory motifs; designing common PCR primers
"""

def longest_common_prefix(sequences):
    """
    Find the longest prefix shared by all sequences.
    """
    if not sequences:
        return ""
    
    prefix = sequences[0]
    for seq in sequences[1:]:
        while not seq.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test
result = longest_common_prefix(["ATGCC", "ATGCACT", "ATGCTT"])
print(f"Longest common prefix: '{result}'")  # Output: 'ATGC'
