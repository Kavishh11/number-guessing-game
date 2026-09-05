# Number Guessing Game

import random

print("===== Number Guessing Game =====")

difficulty = input(
    "Choose the difficulty (1. Easy, 2. Medium, 3. Hard): "
)

max_number = 0
max_attempts = 0

if difficulty == "1":
    max_number = 50
    max_attempts = 10
    print("You selected Easy!")

elif difficulty == "2":
    max_number = 100
    max_attempts = 7
    print("You selected Medium!")

elif difficulty == "3":
    max_number = 200
    max_attempts = 5
    print("You selected Hard!")

else:
    print("Please choose a correct option.")
    exit()

number = random.randint(1, max_number)

print(f"\nI'm thinking of a number between 1 and {max_number}.")
print(f"You have {max_attempts} attempts.")

attempts = 0

while attempts < max_attempts:

    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess == number:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break

    elif guess > number:
        print("Too high!")

    else:
        print("Too low!")

    remaining = max_attempts - attempts

    if remaining > 0:
        print(f"You have {remaining} attempts remaining.")

else:
    print(f"\nGame over! The number was {number}.")
