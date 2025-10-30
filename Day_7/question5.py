"""
### Q5

**Question:** Write a function to convert a list of degrees to radians using the formula: radians = degrees × (π/180).

**Input:** `[0][90][180][270]`

**Expected Output:** `[0.0, 1.57, 3.14, 4.71]` (rounded to 2 decimals)

**Usage:** Converting angles for trigonometric functions in bioinformatics; spatial analysis of molecular structures; signal processing in medical imaging
"""

import math

def degrees_to_radians_explicit(degrees_list):
    pi_over_180 = math.pi / 180
    return [round(deg * pi_over_180, 2) for deg in degrees_list]


result = degrees_to_radians_explicit([0, 90, 180, 270])
print(f"Degrees to radians: {result}")
        