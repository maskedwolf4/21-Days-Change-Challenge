"""
**Q9 - Gene Expression Matrix Normalization**
Question: Given a NumPy array representing gene expression data (genes × samples), normalize each gene using z-score normalization across samples.
Input: `np.array([[100][200][150], [50][75][60], [300][350][320]])`
Expected Output: Normalized array with mean=0 and std=1 for each row
Usage: Preprocessing gene expression data for differential expression analysis
"""

import numpy as np

def normalize_gene_expression(expression_matrix):
    """
    Z-score normalization for gene expression data
    Normalizes each gene (row) across samples (columns)
    """
    # Calculate mean and std for each gene (across samples)
    means = expression_matrix.mean(axis=1, keepdims=True)
    stds = expression_matrix.std(axis=1, keepdims=True)
    
    # Z-score normalization
    normalized = (expression_matrix - means) / stds
    
    return normalized

# Test
data = np.array([[100, 200, 150], 
                 [50, 75, 60], 
                 [300, 350, 320]])

normalized = normalize_gene_expression(data)
print(normalized)
print(f"\nRow means: {normalized.mean(axis=1)}")  # Should be ~0
print(f"Row stds: {normalized.std(axis=1)}")      # Should be ~1
