# Take input from the user for temperature in Celsius
c = int(input("Enter the temperature in Celsius: "))

# Store the multiplication factor for conversion (Celsius to Fahrenheit)
x = 9/5

# Multiply the Celsius temperature by the factor
f = c * x

# Add 32 to complete the conversion formula
f = f + 32

# Print the temperature in Fahrenheit
print(f)
