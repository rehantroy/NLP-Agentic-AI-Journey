# the perfect number guess

import random
number = random.randint(1, 100)

guesses = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the perfect number!")
        print(f"It took you {guesses} guesses.")
        break

