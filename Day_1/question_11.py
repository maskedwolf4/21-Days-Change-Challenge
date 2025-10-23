"""
**Q11 - Time Series Feature Engineering**
Question: Create rolling window features (mean, std, min, max) for sensor data with configurable window sizes using Pandas.
Input: DataFrame with timestamp and sensor values, `window_size=5`
Expected Output: DataFrame with original + 4 new rolling feature columns
Usage: Feature engineering for predictive maintenance and IoT analytics
"""

import pandas as pd

def create_rolling_features(df, value_column, window_size=5):
    """
    Creates rolling window features for time series data
    """
    df = df.copy()
    
    # Create rolling statistics
    df[f'{value_column}_rolling_mean'] = df[value_column].rolling(window=window_size).mean()
    df[f'{value_column}_rolling_std'] = df[value_column].rolling(window=window_size).std()
    df[f'{value_column}_rolling_min'] = df[value_column].rolling(window=window_size).min()
    df[f'{value_column}_rolling_max'] = df[value_column].rolling(window=window_size).max()
    
    return df

# Test
data = {
    'timestamp': pd.date_range('2024-01-01', periods=10, freq='H'),
    'sensor_value': [10, 12, 11, 15, 14, 13, 16, 18, 17, 19]
}

df = pd.DataFrame(data)
result = create_rolling_features(df, 'sensor_value', window_size=5)
print(result)
