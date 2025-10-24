"""
### Q18

**Question:** Create a `Protein` class that stores amino acid sequence and calculates molecular weight, isoelectric point, and hydrophobicity using Kyte-Doolittle scale.

**Input:** `protein = Protein("MKTAYIAKQR"); protein.calculate_properties()`

**Expected Output:** `{"molecular_weight": 1149.36, "pI": 9.75, "hydrophobicity": -0.32}`

**Usage:** Protein characterization in drug discovery and structural biology research.
"""

class Protein:
    """Calculate biochemical properties of proteins"""
    
    # Molecular weights in Daltons
    AA_WEIGHTS = {
        'A': 89.1, 'C': 121.2, 'D': 133.1, 'E': 147.1, 'F': 165.2,
        'G': 75.1, 'H': 155.2, 'I': 131.2, 'K': 146.2, 'L': 131.2,
        'M': 149.2, 'N': 132.1, 'P': 115.1, 'Q': 146.2, 'R': 174.2,
        'S': 105.1, 'T': 119.1, 'V': 117.1, 'W': 204.2, 'Y': 181.2
    }
    
    # Kyte-Doolittle hydrophobicity scale
    HYDROPHOBICITY = {
        'A': 1.8, 'C': 2.5, 'D': -3.5, 'E': -3.5, 'F': 2.8,
        'G': -0.4, 'H': -3.2, 'I': 4.5, 'K': -3.9, 'L': 3.8,
        'M': 1.9, 'N': -3.5, 'P': -1.6, 'Q': -3.5, 'R': -4.5,
        'S': -0.8, 'T': -0.7, 'V': 4.2, 'W': -0.9, 'Y': -1.3
    }
    
    def __init__(self, sequence):
        self.sequence = sequence.upper()
    
    def calculate_properties(self):
        """Calculate molecular weight, pI (simplified), and hydrophobicity"""
        # Molecular weight (subtract water for peptide bonds)
        mw = sum(self.AA_WEIGHTS.get(aa, 0) for aa in self.sequence)
        mw -= 18.015 * (len(self.sequence) - 1)  # Peptide bonds
        
        # Simplified pI calculation (actual calculation is complex)
        # This is a rough approximation
        basic_aa = sum(self.sequence.count(aa) for aa in 'KRH')
        acidic_aa = sum(self.sequence.count(aa) for aa in 'DE')
        pI = 7.0 + (basic_aa - acidic_aa) * 0.5
        
        # Average hydrophobicity
        hydro = sum(self.HYDROPHOBICITY.get(aa, 0) for aa in self.sequence)
        avg_hydro = hydro / len(self.sequence) if self.sequence else 0
        
        return {
            "molecular_weight": round(mw, 2),
            "pI": round(pI, 2),
            "hydrophobicity": round(avg_hydro, 2)
        }

# Usage
protein = Protein("MKTAYIAKQR")
print(protein.calculate_properties())
