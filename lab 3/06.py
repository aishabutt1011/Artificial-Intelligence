# Define a list of numbers
x = [1, 2, 3, 4, 5, 6, 7, 23, 4, 5]

# Initialize counters for even and odd numbers
even = 0
odd = 0

# Loop through each element in the list
for i in range(0, len(x)):
    
    # Check if the current element is even
    if x[i] % 2 == 0:
        even = even + 1  # Increment even counter
    else:
        odd = odd + 1   # Increment odd counter

# Print the total number of even numbers
print("Even numbers are: ", even)

# Print the total number of odd numbers
print("Odd numbers are: ", odd)
