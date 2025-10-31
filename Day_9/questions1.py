"""
## Simple Logic Questions (Q1-Q6)

**Q1: Data Preprocessing - Missing Value Counter**
Question: Write a function that takes a list of sensor readings (which may contain None values) and returns a dictionary with count of valid readings and percentage of missing data.

Input: `[23.5, None, 24.1, None, 23.8, 24.0, None, 23.9]`

Expected Output: `{'valid_readings': 5, 'missing_percentage': 37.5}`

Usage: Used in IoT data preprocessing and sensor data quality assessment before feeding into ML models.[^3]
"""

def missing_valur_counter(data: list) -> dict:
    """A function that takes a list of sensor readings (which may contain None values) and returns a dictionary with count of valid readings and percentage of missing data."""

    count_none = data.count(None)
    n=len(data)
    count_vr = n - count_none
    
    missing_perc = (count_none/n)*100

    ans = {"valid_readings":count_vr, "missing_percentage":missing_perc}

    return ans

print(missing_valur_counter([23.5, None, 24.1, None, 23.8, 24.0, None, 23.9]))