"""
### Q4

**Question:** Create a function that parses a FASTA header line and extracts the sequence ID and description as separate values.

**Input:** `">sp|P12345|PROTEIN_HUMAN Heat shock protein"`

**Expected Output:** `{"id": "sp|P12345|PROTEIN_HUMAN", "description": "Heat shock protein"}`

**Usage:** Preprocessing biological sequence data files for downstream analysis pipelines.
"""

import re

def parse_fasta_header(fasta_header:str) -> dict:
    """A function that parses a FASTA header line and extracts the sequence ID and description as separate values."""

    match = re.match(r'>(\S+)\s+(.*)', fasta_header)

    if match:
        header = match.group(1)
        description = match.group(2)
        
    return {"id": header, "description" : description}

data = parse_fasta_header(">sp|P12345|PROTEIN_HUMAN Heat shock protein")
print(data)