"""
### Q1
**Question:** Write a function to reverse complement a DNA sequence (reverse the string and swap A↔T, G↔C).

**Input:** `"ATGCGA"`

**Expected Output:** `"TCGCAT"`

**Usage:** Analyzing reverse strand in genome assembly, primer design for PCR, processing paired-end sequencing reads
"""

def reverse_compliment(seq:str) -> str:
    """Function to Reverse Compliment DNA"""
    valid = ['A', 'T', 'G', 'C']

    seq = seq.upper()
    if seq not in valid:
        raise TypeError("Enter only DNA Sequence")


    r_com = seq.replace("ATGC","TACG")

    return r_com

r_com = reverse_compliment("ATGCGccccAgA")
print(r_com) #output - TACGGCCCCAGA