"""
### Q1
**Question:** Write a function to calculate the GC content percentage of a DNA sequence (ratio of G and C nucleotides to total length).

**Input:** `"ATGCGCTA"`

**Expected Output:** `50.0`

**Usage:** Basic quality metric in genomics for assessing DNA sequences before analysis.
"""

def count_gc_perc(sequence:str):
    """A function to calculate the GC content percentage of a DNA sequence."""
    sequence.upper()
    sequence.split()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_length = len(sequence)

    # for i,char in enumerate(sequence):
    #     if char == 'G':
    #         g_count = g_count + 1
    #     elif char == 'C':
    #         c_count = c_count + 1
    #     else:
    #         continue

    #     return g_count, c_count


    
    perc = (g_count + c_count)/total_length *100

    return perc

perc = count_gc_perc("ATGCGCTA")
print(perc)
