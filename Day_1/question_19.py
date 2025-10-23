"""
**Q19 - Phylogenetic Tree Distance Matrix**
Question: Build a class `PhylogeneticCalculator` that computes pairwise evolutionary distances between species based on sequence differences.
Input: Dictionary of species names and their sequences
Expected Output: Distance matrix as DataFrame
Usage: Constructing phylogenetic trees in evolutionary biology studies
"""
import pandas as pd
import numpy as np

class PhylogeneticCalculator:
    """Calculates evolutionary distances between species sequences"""
    
    def __init__(self):
        pass
    
    def hamming_distance(self, seq1, seq2):
        """Calculates Hamming distance (number of differences)"""
        if len(seq1) != len(seq2):
            raise ValueError("Sequences must be same length for aligned comparison")
        
        differences = sum(c1 != c2 for c1, c2 in zip(seq1, seq2))
        return differences
    
    def p_distance(self, seq1, seq2):
        """
        Calculates p-distance (proportion of different sites)
        p = differences / total_positions
        """
        differences = self.hamming_distance(seq1, seq2)
        return differences / len(seq1)
    
    def jukes_cantor_distance(self, seq1, seq2):
        """
        Calculates Jukes-Cantor corrected distance
        d = -3/4 * ln(1 - 4/3 * p)
        Accounts for multiple substitutions at same site
        """
        p = self.p_distance(seq1, seq2)
        
        # Avoid log of negative number
        if p >= 0.75:
            return float('inf')  # Sequences too divergent
        
        d = -0.75 * np.log(1 - (4/3) * p)
        return d
    
    def compute_distance_matrix(self, species_dict, method='jukes_cantor'):
        """
        Computes pairwise distance matrix for all species
        
        Args:
            species_dict: {species_name: sequence}
            method: 'hamming', 'p_distance', or 'jukes_cantor'
        """
        species_names = list(species_dict.keys())
        n = len(species_names)
        
        # Initialize distance matrix
        distance_matrix = np.zeros((n, n))
        
        # Calculate pairwise distances
        for i in range(n):
            for j in range(i+1, n):
                seq1 = species_dict[species_names[i]]
                seq2 = species_dict[species_names[j]]
                
                if method == 'hamming':
                    dist = self.hamming_distance(seq1, seq2)
                elif method == 'p_distance':
                    dist = self.p_distance(seq1, seq2)
                else:  # jukes_cantor
                    dist = self.jukes_cantor_distance(seq1, seq2)
                
                distance_matrix[i, j] = dist
                distance_matrix[j, i] = dist  # Symmetric matrix
        
        # Convert to DataFrame for better readability
        df = pd.DataFrame(distance_matrix, 
                         index=species_names, 
                         columns=species_names)
        
        return df

# Test
species_sequences = {
    'Human': 'ATGCGATCGATCG',
    'Chimp': 'ATGCGATCGATCG',
    'Gorilla': 'ATGCGATCGTTCG',
    'Orangutan': 'ATGCGTTCGATCG',
    'Macaque': 'ATGCGTTCGTTCG'
}

calculator = PhylogeneticCalculator()
distance_df = calculator.compute_distance_matrix(species_sequences, method='jukes_cantor')

print("Evolutionary Distance Matrix (Jukes-Cantor):")
print(distance_df.round(4))
print(f"\nMost similar pair: Human-Chimp (distance: {distance_df.loc['Human', 'Chimp']:.4f})")
