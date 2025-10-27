"""
## Q1

**Question:** Write a function to translate a DNA sequence into its corresponding mRNA sequence (replace T with U).

**Input:** `"ATGCAGTTC"`

**Expected Output:** `"AUGCAGUUC"`

**Usage:** Modeling transcription in gene expression studies; generating mRNA templates for in-vitro synthesis; simulating synthetic biology workflows
"""

def reverse_transcript(seq: str) -> str:
    """A function to perform reverse transcription"""
    seq = seq.upper()
    rt_seq = seq.replace('T','U')

    return rt_seq

print(reverse_transcript("ATATCCGCAGTTC"))