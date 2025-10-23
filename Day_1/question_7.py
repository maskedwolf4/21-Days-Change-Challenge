"""
**Q7 - Scientific Unit Converter**
Question: Create a class `BioUnitConverter` that converts between common biological measurement units (ng/ml to mg/L, μM to nM, etc.) with dimensional analysis validation.
Input: `value=500`, `from_unit="ng/ml"`, `to_unit="mg/L"`
Expected Output: `0.5`
Usage: Standardizing measurements across different experimental datasets
"""

class BioUnitConverter:
    """Converts between biological measurement units"""
    
    def __init__(self):
        # Conversion factors to base unit (mg/L for concentration)
        self.conversion_factors = {
            'ng/ml': 0.001,   # ng/ml to mg/L
            'mg/L': 1.0,      # base unit
            'μg/ml': 1.0,     # μg/ml = mg/L
            'μM': None,       # requires molecular weight
            'nM': None        # requires molecular weight
        }
    
    def convert(self, value, from_unit, to_unit):
        """Converts value between units"""
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")
        
        # Convert to base unit (mg/L)
        base_value = value * self.conversion_factors[from_unit]
        
        # Convert from base unit to target unit
        result = base_value / self.conversion_factors[to_unit]
        
        return result

# Test
converter = BioUnitConverter()
result = converter.convert(500, 'ng/ml', 'mg/L')
print(result)  # 0.5
