import random  # Importing the random module to generate random numbers

# Taking input from user for the first guess
x = int(input("Enter guess: "))

# Generating a random number between 1 and 9
y = random.randint(1, 9)

# Loop will continue until the user's guess matches the random number
while(x != y):
    # Asking user to guess again
    x = int(input("Enter guess: "))

# If guess is correct, print success message
print("Well guessed!")
