"""
**Q5: Outlier Detection using IQR**
Question: Write a function that identifies outliers in a numerical dataset using the Interquartile Range (IQR) method. Return list of outlier values.

Input: `[^10][^12][^12][^13][^12][^11][^14][^13][^15][^10][^10][^100][^12]`

Expected Output: `100`

Usage: Used in data cleaning phase before model training to remove anomalies that could skew statistical models and predictions.
"""


def outlier_detection(data: list) -> list:

    n = len(data)

    q1 = (25/100)*(n+1)

    q3 = (75/100)*(n+1)

    iqr = q3 - q1


    ll = q1 - 1.5*iqr

    ul = q3 + 1.5*iqr

    ol = []


    for i in data:
        if i < ll or i > ul:
            ol.append(i)

    return ol

print(outlier_detection([101,10, 12, 12, 13, 12, 11, 14, 13, 15, 10, 10, 100, 12]))

