"""
## Q2

**Question:** Create a function that finds the most frequent nucleotide in a given DNA sequence.

**Input:** `"AAGGCTTAA"`

**Expected Output:** `"A"`

**Usage:** Quality checks in sequencing data; analyzing nucleotide frequency bias; primer design for PCR
"""

def frequent_nucleotide(seq: str) -> str:
    """A unction that finds the most frequent nucleotide in a given DNA sequence."""

    seq = seq.upper()

    f = max(seq)
    
    return f

print(frequent_nucleotide("ATGCCCATG"))