# DATA TYPES AND TYPE CONVERSION IN PYTHON
# The `type()` function tells you what kind of data a variable holds.
# Python supports different data types like int, float, booleans, and complex numbers.


print("\nShowing variable values with their data types:\n")


# 1. Integer type
num1 = 42
print("Value:", num1, "| Type:", type(num1))  # Output: Value: 42 | Type: <class 'int'>

# 2. Negative Integer
num2 = -7
print("Value:", num2, "| Type:", type(num2))  # Output: Value: -7 | Type: <class 'int'>

# 3. Zero as Integer
num3 = 0
print("Value:", num3, "| Type:", type(num3))  # Output: Value: 0 | Type: <class 'int'>


# 4. Float type
decimal1 = 3.14
print("Value:", decimal1, "| Type:", type(decimal1))  # Output: Value: 3.14 | Type: <class 'float'>

# 5. Scientific notation Float
decimal2 = 2.5e3  # 2.5 × 1000 = 2500.0
print("Value:", decimal2, "| Type:", type(decimal2))  # Output: Value: 2500.0 | Type: <class 'float'>
# 6. Negative Float
decimal3 = -0.99
print("Value:", decimal3, "| Type:", type(decimal3))  # Output: Value: -0.99 | Type: <class 'float'>


# 7. Boolean True
bool1 = True
print("Value:", bool1, "| Type:", type(bool1))  # Output: Value: True | Type: <class 'bool'>

# 8. Boolean False
bool2 = False
print("Value:", bool2, "| Type:", type(bool2))  # Output: Value: False | Type: <class 'bool'>

# 9. Complex number
complex1 = 4 + 2j
print("Value:", complex1, "| Type:", type(complex1))   # Output: Value: (4+2j) | Type: <class 'complex'>

# 10. Purely imaginary complex number
complex2 = -3j
print("Value:", complex2, "| Type:", type(complex2))  # Output: Value: (-0-3j) | Type: <class 'complex'>

# 11. Converting values to Booleans
convert1 = bool(0)  # 0 becomes False
print("Convert 1 (from 0):", convert1, "| Type:", type(convert1))  # Output: Convert 1 (from 0): False | Type: <class 'bool'>

convert2 = bool(10)  # Any non-zero number becomes True
print("Convert 2 (from 10):", convert2, "| Type:", type(convert2))  # Output: Convert 2 (from 10): True | Type: <class 'bool'>

convert3 = bool("")  # Empty string becomes False
print("Convert 3 (from empty string):", convert3, "| Type:", type(convert3))  # Output: Convert 3 (from empty string): False | Type: <class 'bool'>

convert4 = bool("Hello")  # Non-empty string becomes True
print("Convert 4 (from 'Hello'):", convert4, "| Type:", type(convert4))  # Output: Convert 4 (from 'Hello'): True | Type: <class 'bool'>
