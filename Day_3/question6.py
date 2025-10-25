"""
### Q6
**Question:** Create a function that converts a sequence to k-mer frequency dictionary (subsequences of length k).

**Input:** `sequence="ATGCATG", k=3`

**Expected Output:** `{"ATG": 2, "TGC": 1, "GCA": 1, "CAT": 1}`

*Usage:** Feature extraction for genome classification, identifying DNA motifs, training language models on biological sequences
"""

def k_mer_dict(seq:str, k:int) -> dict:
    """A function that converts a sequence to k-mer frequency dictionary (subsequences of length k)."""

    kmer_dict = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        kmer_dict[kmer] = kmer_dict.get(kmer, 0) + 1
    return kmer_dict

# Test
print(k_mer_dict("ATGCATG", 3))