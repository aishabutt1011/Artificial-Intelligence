# Define a function to print Fibonacci series up to a given limit
def fibonacci_series(limit):
    
    # Initialize the first two terms of the Fibonacci series
    a, b = 1, 1
    
    # Loop until the value of 'a' exceeds the limit
    while a <= limit:
        
        # Print the current term followed by a space (without a new line)
        print(a, end=" ")
        
        # Store the current value of 'a' in a temporary variable
        temp = a
        
        # Update 'a' with the value of 'b'
        a = b
        
        # Update 'b' with the sum of previous 'a' and 'b'
        b = temp + b

# Call the function and print Fibonacci series up to 50
fibonacci_series(50)
