"""
### Q3

**Question:** Write a function to encode a DNA sequence using run-length encoding (compress consecutive identical bases).

**Input:** `"AAAAGGGCCCTTTT"`

**Expected Output:** `"A4G3C3T4"`

**Usage:** Compressing repetitive genomic sequences; reducing storage for homopolymer regions; efficient representation of microsatellites
"""

def run_length_encode_dna(sequence):
    """
    Compress DNA sequence using run-length encoding.
    Format: base followed by count
    """
    if not sequence:
        return ""
    
    encoded = []
    current_base = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == current_base:
            count += 1
        else:
            encoded.append(f"{current_base}{count}")
            current_base = sequence[i]
            count = 1
    
    # Append the last run
    encoded.append(f"{current_base}{count}")
    
    return ''.join(encoded)

# Test
result = run_length_encode_dna("AAAAGGGCCCTTTT")
print(f"Encoded: {result}")  # Output: A4G3C3T4
