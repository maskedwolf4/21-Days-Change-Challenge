"""
### Q21

**Question:** Create a `ProteinStructure` class that parses PDB file format, extracts alpha carbon coordinates, and calculates inter-residue distances and contact maps.

**Input:** PDB file content as string

**Expected Output:** Contact map as 2D numpy array where 1 indicates residues within 8Å

**Usage:** Protein structure analysis and machine learning feature extraction for structure prediction.
"""

import numpy as np

class ProteinStructure:
    """Parse PDB files and calculate structural properties"""
    
    def __init__(self, pdb_content):
        self.pdb_content = pdb_content
        self.ca_coords = []
        self.residues = []
    
    def parse_pdb(self):
        """Extract alpha carbon coordinates from PDB"""
        for line in self.pdb_content.split('\n'):
            if line.startswith('ATOM') and ' CA ' in line:
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                res_num = int(line[22:26].strip())
                
                self.ca_coords.append([x, y, z])
                self.residues.append(res_num)
        
        self.ca_coords = np.array(self.ca_coords)
        return self
    
    def calculate_distance_matrix(self):
        """Calculate pairwise distances between residues"""
        n = len(self.ca_coords)
        dist_matrix = np.zeros((n, n))
        
        for i in range(n):
            for j in range(i+1, n):
                dist = np.linalg.norm(self.ca_coords[i] - self.ca_coords[j])
                dist_matrix[i, j] = dist
                dist_matrix[j, i] = dist
        
        return dist_matrix
    
    def calculate_contact_map(self, threshold=8.0):
        """Generate contact map (1 if within threshold, 0 otherwise)"""
        dist_matrix = self.calculate_distance_matrix()
        contact_map = (dist_matrix < threshold).astype(int)
        np.fill_diagonal(contact_map, 0)  # Exclude self-contacts
        return contact_map

# Usage
pdb_content = """
ATOM      1  CA  ALA A   1      10.000  10.000  10.000  1.00 20.00           C
ATOM      2  CA  GLY A   2      13.000  11.000  12.000  1.00 20.00           C
"""
structure = ProteinStructure(pdb_content)
structure.parse_pdb()
contact_map = structure.calculate_contact_map(threshold=8.0)
print(contact_map)
