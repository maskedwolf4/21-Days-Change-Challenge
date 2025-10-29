"""
### Q1

**Question:** Write a function to count the number of codons (triplets) in a given DNA sequence, ignoring any trailing bases that do not form a complete codon.

**Input:** `"ATGCGTAACTAG"`

**Expected Output:** `4`

**Usage:** Parsing coding regions for translation; identifying possible open reading frames; analyzing frameshift mutations
"""

def count_codons(dna_seq):
    """
    Count complete codons (triplets) in DNA sequence.
    Each codon represents 3 bases that code for an amino acid.
    """
    # Length must be divisible by 3 for complete codons
    complete_length = (len(dna_seq) // 3) * 3
    return complete_length // 3

# Test
result = count_codons("ATGCGTAACTAG")
print(f"Number of codons: {result}")  # Output: 4
