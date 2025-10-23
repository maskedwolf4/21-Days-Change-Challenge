"""
**Q21 - Codon Usage Bias Calculator**
Question: Implement a class `CodonAnalyzer` that calculates codon usage frequency and Relative Synonymous Codon Usage (RSCU) for a given DNA sequence.
Input: DNA sequence string
Expected Output: Dictionary of codon frequencies and RSCU values
Usage: Gene expression optimization and synthetic biology applications
"""

from collections import defaultdict

class CodonAnalyzer:
    """Analyzes codon usage patterns in DNA sequences"""
    
    def __init__(self):
        # Standard genetic code
        self.genetic_code = {
            'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
            'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
            'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
            'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
            'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
            'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
            'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
            'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
            'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
        }
        
        # Group codons by amino acid
        self.aa_to_codons = defaultdict(list)
        for codon, aa in self.genetic_code.items():
            self.aa_to_codons[aa].append(codon)
    
    def count_codons(self, sequence):
        """Counts frequency of each codon in sequence"""
        sequence = sequence.upper().replace(' ', '')
        
        if len(sequence) % 3 != 0:
            raise ValueError("Sequence length must be multiple of 3")
        
        codon_counts = defaultdict(int)
        
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            if codon in self.genetic_code:
                codon_counts[codon] += 1
        
        return dict(codon_counts)
    
    def calculate_rscu(self, sequence):
        """
        Calculates Relative Synonymous Codon Usage (RSCU)
        
        RSCU = (observed frequency of codon) / (expected frequency if no bias)
        RSCU = (X_ij * n_i) / sum(X_ij for all synonymous codons)
        
        where:
        X_ij = count of codon j for amino acid i
        n_i = number of synonymous codons for amino acid i
        """
        codon_counts = self.count_codons(sequence)
        
        # Count amino acids
        aa_counts = defaultdict(int)
        for codon, count in codon_counts.items():
            aa = self.genetic_code[codon]
            if aa != '*':  # Exclude stop codons
                aa_counts[aa] += count
        
        # Calculate RSCU
        rscu_values = {}
        
        for aa, total_count in aa_counts.items():
            synonymous_codons = self.aa_to_codons[aa]
            num_synonymous = len(synonymous_codons)
            
            for codon in synonymous_codons:
                codon_count = codon_counts.get(codon, 0)
                
                if total_count > 0:
                    rscu = (codon_count * num_synonymous) / total_count
                else:
                    rscu = 0
                
                rscu_values[codon] = {
                    'amino_acid': aa,
                    'count': codon_count,
                    'rscu': round(rscu, 3)
                }
        
        return rscu_values
    
    def identify_preferred_codons(self, rscu_values, threshold=1.0):
        """Identifies preferred codons (RSCU > threshold)"""
        preferred = {}
        
        for codon, data in rscu_values.items():
            if data['rscu'] > threshold:
                preferred[codon] = data
        
        return preferred

# Test
sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

analyzer = CodonAnalyzer()
codon_freq = analyzer.count_codons(sequence)
print("Codon Frequencies:")
for codon, count in sorted(codon_freq.items()):
    print(f"{codon}: {count}")

rscu = analyzer.calculate_rscu(sequence)
print("\nRSCU Values (sample):")
for codon in list(rscu.keys())[:5]:
    print(f"{codon} ({rscu[codon]['amino_acid']}): {rscu[codon]['rscu']}")

preferred = analyzer.identify_preferred_codons(rscu, threshold=1.0)
print(f"\nPreferred codons: {len(preferred)}")
