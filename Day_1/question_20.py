"""
**Q20 - Protein Structure Contact Map**
Question: Create a class `ContactMapGenerator` that identifies residue-residue contacts in a protein structure based on distance thresholds.
Input: List of 3D coordinates for each residue, distance threshold
Expected Output: Binary contact matrix
Usage: Protein structure analysis and fold prediction
"""

import numpy as np

class ContactMapGenerator:
    """Generates residue contact maps from protein structures"""
    
    def __init__(self, distance_threshold=8.0):
        """
        Args:
            distance_threshold: Distance cutoff in Angstroms for defining contacts
        """
        self.distance_threshold = distance_threshold
    
    def calculate_distance(self, coord1, coord2):
        """Calculates Euclidean distance between two 3D coordinates"""
        return np.sqrt(sum((a - b) ** 2 for a, b in zip(coord1, coord2)))
    
    def generate_contact_map(self, residue_coordinates):
        """
        Generates binary contact map from residue coordinates
        
        Args:
            residue_coordinates: List of (x, y, z) tuples for each residue
            
        Returns:
            Binary contact matrix (numpy array)
        """
        n_residues = len(residue_coordinates)
        contact_map = np.zeros((n_residues, n_residues), dtype=int)
        
        for i in range(n_residues):
            for j in range(i + 1, n_residues):
                distance = self.calculate_distance(
                    residue_coordinates[i], 
                    residue_coordinates[j]
                )
                
                # Mark as contact if within threshold
                if distance <= self.distance_threshold:
                    contact_map[i, j] = 1
                    contact_map[j, i] = 1  # Symmetric
        
        return contact_map
    
    def get_contact_list(self, contact_map):
        """Converts contact map to list of contacting residue pairs"""
        contacts = []
        n = contact_map.shape[0]
        
        for i in range(n):
            for j in range(i + 1, n):
                if contact_map[i, j] == 1:
                    contacts.append((i, j))
        
        return contacts
    
    def calculate_contact_order(self, contact_map):
        """
        Calculates relative contact order (measure of protein topology)
        RCO = sum(|i-j|) / (N * L)
        where N is number of contacts, L is sequence length
        """
        contacts = self.get_contact_list(contact_map)
        
        if len(contacts) == 0:
            return 0.0
        
        n_residues = contact_map.shape[0]
        sequence_separation_sum = sum(abs(j - i) for i, j in contacts)
        
        rco = sequence_separation_sum / (len(contacts) * n_residues)
        return rco

# Test
# Simulating alpha helix with some contacts
coordinates = [
    (0.0, 0.0, 0.0),
    (1.5, 1.0, 1.5),
    (2.0, 2.5, 3.0),
    (2.5, 4.0, 4.5),
    (3.0, 5.5, 6.0),
    (4.0, 7.0, 7.5),
    (5.0, 8.5, 9.0),
    (6.5, 10.0, 10.5)
]

generator = ContactMapGenerator(distance_threshold=8.0)
contact_map = generator.generate_contact_map(coordinates)

print("Contact Map:")
print(contact_map)

contacts = generator.get_contact_list(contact_map)
print(f"\nNumber of contacts: {len(contacts)}")
print(f"Contact pairs: {contacts}")

rco = generator.calculate_contact_order(contact_map)
print(f"\nRelative Contact Order: {rco:.3f}")
