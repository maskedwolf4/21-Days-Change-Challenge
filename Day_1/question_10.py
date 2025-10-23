"""
*Q10 - Clinical Trial Data Aggregation**
Question: Using Pandas, aggregate patient data by treatment group and calculate mean, std, and count for multiple biomarkers.
Input: DataFrame with columns `[patient_id, treatment_group, biomarker_A, biomarker_B, age]`
Expected Output: Grouped statistics DataFrame
Usage: Statistical analysis in clinical research and drug efficacy studies
"""

import pandas as pd 
import numpy as np

def aggregate_clinical_data(df):
    """
    Aggregates patient data by treatment group with statistics
    """
    # Group by treatment and calculate statistics
    agg_dict = {
        'biomarker_A': ['mean', 'std', 'count'],
        'biomarker_B': ['mean', 'std', 'count'],
        'age': ['mean', 'std', 'count']
    }
    
    result = df.groupby('treatment_group').agg(agg_dict)
    
    # Flatten column names
    result.columns = ['_'.join(col).strip() for col in result.columns.values]
    
    return result.round(2)

# Test
data = {
    'patient_id': [1, 2, 3, 4, 5, 6],
    'treatment_group': ['A', 'A', 'A', 'B', 'B', 'B'],
    'biomarker_A': [12.5, 13.1, 11.9, 15.2, 14.8, 15.5],
    'biomarker_B': [8.3, 8.7, 8.1, 9.2, 9.5, 9.1],
    'age': [45, 52, 48, 55, 59, 53]
}

df = pd.DataFrame(data)
result = aggregate_clinical_data(df)
print(result)
