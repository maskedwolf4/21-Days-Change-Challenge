"""
**Q12 - Missing Data Imputation Strategy**
Question: Implement multiple imputation strategies (mean, median, forward-fill, interpolate) for a dataset and compare resulting distributions using NumPy/Pandas.
Input: DataFrame with missing values in multiple columns
Expected Output: Dictionary of imputed DataFrames with strategy names as keys
Usage: Data preprocessing in machine learning pipelines with incomplete datasets
"""

import pandas as pd
import numpy as np

class ImputationComparer:
    """Compares multiple imputation strategies"""
    
    def __init__(self, df):
        self.df = df.copy()
        self.imputed_dfs = {}
    
    def mean_imputation(self):
        """Fill missing values with column mean"""
        df_imputed = self.df.copy()
        for col in df_imputed.select_dtypes(include=[np.number]).columns:
            df_imputed[col].fillna(df_imputed[col].mean(), inplace=True)
        return df_imputed
    
    def median_imputation(self):
        """Fill missing values with column median"""
        df_imputed = self.df.copy()
        for col in df_imputed.select_dtypes(include=[np.number]).columns:
            df_imputed[col].fillna(df_imputed[col].median(), inplace=True)
        return df_imputed
    
    def forward_fill(self):
        """Forward fill missing values"""
        return self.df.fillna(method='ffill')
    
    def interpolate(self):
        """Linear interpolation for missing values"""
        return self.df.interpolate(method='linear')
    
    def compare_all(self):
        """Apply all strategies and return dictionary"""
        self.imputed_dfs['mean'] = self.mean_imputation()
        self.imputed_dfs['median'] = self.median_imputation()
        self.imputed_dfs['forward_fill'] = self.forward_fill()
        self.imputed_dfs['interpolate'] = self.interpolate()
        
        return self.imputed_dfs

# Test
data = {
    'feature1': [1, 2, np.nan, 4, 5],
    'feature2': [10, np.nan, 30, np.nan, 50]
}

df = pd.DataFrame(data)
comparer = ImputationComparer(df)
results = comparer.compare_all()

for strategy, df_result in results.items():
    print(f"\n{strategy.upper()}:")
    print(df_result)
