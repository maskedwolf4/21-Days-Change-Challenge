"""
### Q2

**Question:** Create a function that converts temperature readings from Celsius to Kelvin and Fahrenheit, returning a dictionary with all three scales.

**Input:** `25.0`

**Expected Output:** `{"celsius": 25.0, "kelvin": 298.15, "fahrenheit": 77.0}`

**Usage:** Environmental data normalization in climate modeling and experimental data preprocessing.
"""

try :
    def temp_convert(temperature:float) -> dict:
        """A function that converts temperature readings from Celsius to Kelvin and Fahrenheit"""

        kelvin = temperature + 273.15

        fahreheit = (temperature * 9/5) + 32

        conversion = {
            "celsius" : float(temperature),
            "kelvin" : kelvin,
            "fahreinheit" : fahreheit
        }

        return conversion
except TypeError as e:
    raise TypeError

temp = temp_convert(25)
print(temp)