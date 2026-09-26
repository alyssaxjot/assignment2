import random

# Generate a random integer between 1 and 25 inclusive
secret_number = random.randint(1, 25)

# Give user up to 5 attempts to guess
for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}/5 - Guess a number between 1 and 25: "))
    
    if guess == secret_number:
        print("Correct! You win!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    # If the loop finishes without a break, the user ran out of guesses
    print(f"Sorry, you ran out of guesses. The correct number was {secret_number}.")
