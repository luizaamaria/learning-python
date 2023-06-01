'''

Define a  water_state function that:

1. gets a temperature argument

2. returns the string "Solid" if the temperature is less than or equal to 0

3. returns "Liquid" if the temperature is greater than 0, but less than 100.

4. returns "Gas" if the temperature is greater than or equal to 100.

'''


def water_state(temperature):
    # Check if the temperature is less than or equal to 0
    if temperature <= 0:
        return "Solid"  # Return "Solid" if temperature is <= 0
    # Check if the temperature is between 0 and 100 (exclusive)
    elif 0 < temperature < 100:
        return "Liquid"  # Return "Liquid" if temperature is between 0 and 100
    else:
        return "Gas"  # Return "Gas" for all other cases
