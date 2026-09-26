import random

# Generate a random integer between 1 and 10 inclusive
secret_number = random.randint(1, 10)

# Prompt the user for a single guess
guess = int(input("Guess a number between 1 and 10: "))

# Check if the guess matches the secret number
if guess == secret_number:
    print(f"Correct! The number was {secret_number}.")
else:
    print(f"Sorry, that's incorrect. The number was {secret_number}.")
