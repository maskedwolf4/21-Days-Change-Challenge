"""
### Q5

**Question:** Write a function to split a string into chunks of specified length, padding the last chunk if necessary.

**Input:** `text="ATGCGTA", chunk_size=3, padding="N"`

**Expected Output:** `["ATG", "CGT", "ANN"]`

**Usage:** Partitioning sequences for parallel processing; creating k-mer windows for analysis; batch processing in sequence alignment pipelines
"""

def chunk_string_with_padding(text, chunk_size, padding):
    """
    Split string into fixed-size chunks, padding the last chunk.
    """
    chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        
        # Pad last chunk if needed
        if len(chunk) < chunk_size:
            chunk += padding * (chunk_size - len(chunk))
        
        chunks.append(chunk)
    
    return chunks

# Test
result = chunk_string_with_padding("ATGCGTA", 3, "N")
print(f"Chunks: {result}")  # Output: ['ATG', 'CGT', 'ANN']
