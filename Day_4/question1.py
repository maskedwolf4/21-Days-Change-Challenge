"""
### Q1

**Question:** Write a function to calculate the melting temperature (Tm) of a DNA primer using the basic formula: Tm = 4(G+C) + 2(A+T).

**Input:** `"ATGCGCTA"`

**Expected Output:** `24`

**Usage:** Designing PCR primers, optimizing annealing temperatures in molecular cloning, planning CRISPR guide RNAs
"""

def melting_temperature(seq: str) -> int:
    """A function to calculate the melting temperature (Tm) of a DNA primer."""
    seq = seq.upper()
    countA = seq.count("A")
    countT = seq.count("T")
    countG = seq.count("G")
    countC = seq.count("C")

    tm = ((4*(countG+countC)) + (2*(countA + countT)))

    return tm

print(melting_temperature("ATGCGCTAGGAAAT")) #40
