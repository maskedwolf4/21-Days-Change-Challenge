"""
**Q1 - Protein Sequence Validator**
Question: Write a function that validates if a given string is a valid protein sequence (contains only standard amino acid codes: ACDEFGHIKLMNPQRSTVWY).
Input: `"MKTAYIAKQRQ"`, `"MKTAYIAKQRQZ"`
Expected Output: `True`, `False`
Usage: Input validation for bioinformatics pipelines processing protein data
"""

# Solution

def validate_protein_sequence(sequence):
    """Validates if a string contains only valid amino acid codes"""
    valid_amino_acids = set('ACDEFGHIKLMNPQRSTVWY')
    return all(char in valid_amino_acids for char in sequence.upper())

# Test
print(validate_protein_sequence("MKTAYIAKQRQ"))  # True
print(validate_protein_sequence("MKTAYIAKQRQZ"))  # False


