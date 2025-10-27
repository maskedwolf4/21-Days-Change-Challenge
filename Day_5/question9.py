"""
### Q9

**Question:** Write a function to parse a FASTA formatted string and return a dictionary with sequence names as keys and sequences as values.

**Input:** `">seq1\nATGCA\n>seq2\nGGGTT"`

**Expected Output:** `{"seq1": "ATGCA", "seq2": "GGGTT"}`

**Usage:** Handling genomic and proteomic datasets; data ingestion for bioinformatics pipelines; workflow automation in sequence analysis
"""

def parse_fasta(fasta):
    result = {}
    name = None
    seqs = []
    for line in fasta.strip().splitlines():
        if line.startswith('>'):
            if name:
                result[name] = ''.join(seqs)
            name = line[1:].strip()
            seqs = []
        else:
            seqs.append(line.strip())
    if name:
        result[name] = ''.join(seqs)
    return result
