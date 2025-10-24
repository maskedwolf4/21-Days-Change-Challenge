"""
### Q20

**Question:** Build a `PhylogeneticTree` class that constructs a UPGMA tree from a distance matrix and outputs the tree in Newick format.

**Input:** Distance matrix as nested list/array

**Expected Output:** Newick format string representing the hierarchical tree

**Usage:** Evolutionary analysis and species relationship visualization in phylogenetics.
"""

import numpy as np

class PhylogeneticTree:
    """Construct phylogenetic trees using UPGMA"""
    
    def __init__(self, distance_matrix, labels):
        self.distance_matrix = np.array(distance_matrix, dtype=float)
        self.labels = labels
    
    def build_tree(self):
        """Build UPGMA tree and return Newick format"""
        n = len(self.labels)
        clusters = {i: (self.labels[i], 1) for i in range(n)}
        distances = self.distance_matrix.copy()
        heights = {i: 0.0 for i in range(n)}
        
        cluster_id = n
        
        while len(clusters) > 1:
            # Find minimum distance
            min_dist = float('inf')
            min_i, min_j = -1, -1
            
            for i in clusters:
                for j in clusters:
                    if i < j and distances[i, j] < min_dist:
                        min_dist = distances[i, j]
                        min_i, min_j = i, j
            
            # Merge clusters
            name_i, size_i = clusters[min_i]
            name_j, size_j = clusters[min_j]
            
            # Calculate new height
            new_height = min_dist / 2
            branch_i = new_height - heights[min_i]
            branch_j = new_height - heights[min_j]
            
            # Create new cluster
            new_name = f"({name_i}:{branch_i:.4f},{name_j}:{branch_j:.4f})"
            new_size = size_i + size_j
            clusters[cluster_id] = (new_name, new_size)
            heights[cluster_id] = new_height
            
            # Update distance matrix
            for k in clusters:
                if k != min_i and k != min_j and k != cluster_id:
                    new_dist = (distances[min_i, k] * size_i + 
                               distances[min_j, k] * size_j) / new_size
                    distances[k, cluster_id] = new_dist
                    distances[cluster_id, k] = new_dist
            
            # Remove old clusters
            del clusters[min_i]
            del clusters[min_j]
            cluster_id += 1
        
        # Return Newick format
        final_tree = list(clusters.values())[0][0]
        return final_tree + ";"

# Usage
distance_matrix = [
    [0, 2, 4, 6],
    [2, 0, 4, 6],
    [4, 4, 0, 6],
    [6, 6, 6, 0]
]
labels = ["A", "B", "C", "D"]
tree = PhylogeneticTree(distance_matrix, labels)
newick = tree.build_tree()
print(newick)
