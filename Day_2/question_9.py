"""
### Q9

**Question:** Given a pandas DataFrame of gene expression data with samples as rows and genes as columns, normalize each gene (column) using z-score normalization.

**Input:** DataFrame with shape (100, 50) containing raw expression values

**Expected Output:** DataFrame with same shape where each column has mean=0 and std=1

**Usage:** Preprocessing gene expression matrices before clustering or differential expression analysis.
"""

import pandas as pd
import numpy as np

def normalize_gene_expression(df):
    """Z-score normalize gene expression data (columns)"""
    # Z-score formula: (x - mean) / std
    normalized_df = (df - df.mean()) / df.std()
    return normalized_df

# Usage
# Assuming df is a DataFrame with shape (100, 50)
df = pd.DataFrame(np.random.rand(100, 50))
normalized = normalize_gene_expression(df)
print(normalized.mean().round(10))  # All approximately 0
print(normalized.std().round(10))   # All approximately 1
