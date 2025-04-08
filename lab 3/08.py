# Loop through numbers from 0 to 6
for i in range(0, 7):
    
    # If i is 3 or 6, skip that iteration using continue
    if(i == 3 or i == 6):
        continue  # Skip the rest of the loop and go to the next iteration

    # Print the value of i (except 3 and 6)
    print(i)
