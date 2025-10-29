"""
### Q5

**Question:** Write a function to check if a DNA sequence is palindromic (its reverse complement is identical to the original).

**Input:** `"GTATAC"`

**Expected Output:** `True`

**Usage:** Detecting restriction enzyme recognition sites; studying regulatory motifs; identifying palindromic repeats in genomes
"""

def is_dna_palindrome(seq):
    """
    Check if DNA sequence reads the same forwards and backwards on reverse complement.
    """
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # Reverse complement
    rev_comp = ''.join(complement.get(base, base) for base in reversed(seq.upper()))
    
    return seq.upper() == rev_comp

# Test
result = is_dna_palindrome("GTATAC")
print(f"Is palindrome: {result}")  # Output: True
