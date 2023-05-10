# Dictionary to store the conversion factors
# for different units of mass and volume
conversion_factors = {
    'kg': 1000,
    'g': 1,
    'mg': 0.001,
    'L': 1000,
    'mL': 1
}

# Function to convert between metric units
def convert_metric_unit(amount, from_unit, to_unit):
    # Convert the amount to the base unit of grams or milliliters
    base_amount = amount * conversion_factors[from_unit]
    # Convert the amount from the base unit to the desired unit
    converted_amount = base_amount / conversion_factors[to_unit]
    return converted_amount

# Example usage
amount = 2 # in kg
from_unit = 'kg'
to_unit = 'g'
converted_amount = convert_metric_unit(amount, from_unit, to_unit)
print(f"{amount} {from_unit} is equal to {converted_amount} {to_unit}")

# Example usage
amount = 1000 # in mg
from_unit = 'mg'
to_unit = 'g'
converted_amount = convert_metric_unit(amount, from_unit, to_unit)
print(f"{amount} {from_unit} is equal to {converted_amount} {to_unit}")