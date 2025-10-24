"""
### Q5

**Question:** Create a `SequenceValidator` class that validates DNA, RNA, and protein sequences. Include methods to check sequence type and validate characters.

**Input:** `validator = SequenceValidator("ATGCN"); validator.validate()`

**Expected Output:** `{"valid": True, "type": "DNA", "ambiguous_bases": 1}`

**Usage:** Input validation in sequencing pipelines before storing data in databases.
"""

class SequenceValidator:
    """Validates DNA, RNA, and protein sequences"""
    
    DNA_BASES = set('ATGCNRYSWKMBDHV')
    RNA_BASES = set('AUGCNRYSWKMBDHV')
    AMINO_ACIDS = set('ACDEFGHIKLMNPQRSTVWYX')
    
    def __init__(self, sequence):
        self.sequence = sequence.upper()
    
    def validate(self):
        """Validate sequence and determine type"""
        seq_set = set(self.sequence)
        
        if seq_set <= self.DNA_BASES:
            ambiguous = len([b for b in self.sequence if b in 'NRYSWKMBDHV'])
            return {"valid": True, "type": "DNA", "ambiguous_bases": ambiguous}
        elif seq_set <= self.RNA_BASES:
            ambiguous = len([b for b in self.sequence if b in 'NRYSWKMBDHV'])
            return {"valid": True, "type": "RNA", "ambiguous_bases": ambiguous}
        elif seq_set <= self.AMINO_ACIDS:
            return {"valid": True, "type": "Protein", "ambiguous_bases": 0}
        else:
            return {"valid": False, "type": "Unknown", "ambiguous_bases": 0}

# Usage
validator = SequenceValidator("ATGCN")
print(validator.validate())  # {"valid": True, "type": "DNA", "ambiguous_bases": 1}

        
        