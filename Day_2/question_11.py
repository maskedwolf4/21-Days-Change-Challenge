"""
### Q11

**Question:** Create a function that reads a CSV of clinical trial data, handles missing values using median imputation for numeric columns and mode for categorical, then returns cleaned DataFrame.

**Input:** CSV file path with mixed data types and missing values

**Expected Output:** Cleaned DataFrame with no missing values

**Usage:** Data preprocessing in healthcare analytics and clinical research studies.
"""

import pandas as pd
import numpy as np

def clean_clinical_data(csv_path):
    """Handle missing values using median/mode imputation"""
    df = pd.read_csv(csv_path)
    
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            # Numeric: use median
            df[column].fillna(df[column].median(), inplace=True)
        else:
            # Categorical: use mode
            mode_value = df[column].mode()
            if len(mode_value) > 0:
                df[column].fillna(mode_value[0], inplace=True)
    
    return df

# Usage
cleaned_df = clean_clinical_data('clinical_data.csv')
print(cleaned_df.isnull().sum())  # All zeros
