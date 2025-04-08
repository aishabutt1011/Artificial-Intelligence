# Prompt the user to enter the number of rows
m = int(input("Enter number of rows: "))  

# Prompt the user to enter the number of columns
n = int(input("Enter number of columns: "))  

# Initialize an empty list to store the result (2D array)
result = []

# Loop through each row
for i in range(m):
    # Create an empty list to represent the current row
    row = []
    
    # Loop through each column
    for j in range(n):
        # Multiply the row index (i) by the column index (j) and append to the row
        row.append(i * j) 
    
    # Append the row to the result
    result.append(row)

# Print the final 2D array (result)
print(result)
