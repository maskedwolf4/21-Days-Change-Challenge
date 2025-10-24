"""
### Q12

**Question:** Build a function that takes a pandas DataFrame of time-series stock prices and calculates rolling mean, standard deviation, and Bollinger Bands (mean ± 2*std) for a given window.

**Input:** DataFrame with 'date' and 'price' columns, window=20

**Expected Output:** DataFrame with additional columns for rolling_mean, rolling_std, upper_band, lower_band

**Usage:** Technical analysis in quantitative finance and trading algorithm development.
"""

import pandas as pd
import numpy as np

def calculate_bollinger_bands(df, window=20):
    """Calculate rolling statistics and Bollinger Bands"""
    result = df.copy()
    
    # Calculate rolling statistics
    result['rolling_mean'] = df['price'].rolling(window=window).mean()
    result['rolling_std'] = df['price'].rolling(window=window).std()
    
    # Calculate Bollinger Bands (mean ± 2*std)
    result['upper_band'] = result['rolling_mean'] + (2 * result['rolling_std'])
    result['lower_band'] = result['rolling_mean'] - (2 * result['rolling_std'])
    
    return result

# Usage
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=100),
    'price': np.random.randn(100).cumsum() + 100
})
bollinger_df = calculate_bollinger_bands(df, window=20)
