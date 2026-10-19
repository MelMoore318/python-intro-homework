# Mini-project: Fahrenheit to Celsius Temperature Converter

# Ask the user for a temperature in Fahrenheit.
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius.
celsius = (fahrenheit - 32) * 5 / 9

# Print the result rounded to one decimal place.
print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C.")
