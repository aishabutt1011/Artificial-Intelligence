# Loop through numbers from 1500 to 2700 (including 2700)
for i in range(1500, 2701):
    
    # Check if the number is divisible by both 7 and 5
    if (i % 7 == 0 and i % 5 == 0):
        
        # If true, print the number
        print(i)
