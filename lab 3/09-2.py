# Loop through numbers from 1 to 50
for i in range(1, 51):
    
    # If 'i' is divisible by both 3 and 5
    if(i % 5 == 0 and i % 3 == 0):
        print("Fizzbuzz")  # Print Fizzbuzz
    
    # If 'i' is divisible by 3 only
    elif(i % 3 == 0):
        print("Fizz")  # Print Fizz
    
    # If 'i' is divisible by 5 only
    elif(i % 5 == 0):
        print("Buzz")  # Print Buzz
    
    # If 'i' is not divisible by 3 or 5
    else:
        print(i)  # Print the number itself
