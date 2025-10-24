"""
### Q3

**Question:** Write a function to calculate the Hamming distance between two equal-length strings (number of positions at which corresponding characters differ).

**Input:** `"AGCT", "AACT"`

**Expected Output:** `1`

**Usage:** Measuring sequence similarity in bioinformatics and error detection in data transmission.
"""

def hamming_distance(seq1:str, seq2:str) -> int :
    """A function to calculate the Hamming distance between two equal-length strings"""

    if len(seq1) != len(seq2):
        raise ValueError("Sequence Must be of equal length")
    
    seq1_list = list(seq1)
    seq2_list = list(seq2)
    
    count = 0
    for i,j in zip(seq1_list,seq2_list):
        if  i != j:
            count = count +1
        
        count
    
    return count

dist  = hamming_distance("AGAT", "AACT")
print(dist)
    
