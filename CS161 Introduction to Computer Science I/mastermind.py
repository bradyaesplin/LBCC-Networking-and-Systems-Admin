"""Mastermind.py, a 4-digit code guessing game.

Progam is based off of a board game called Master Mind, but played using
digits not colors. Program will generate a random four digit number. User
will guess the four digit number, program will error check answers and
display feedback. After 12 tries, print a 'lose' message.
By Brady Esplin CS161 MWF 0800-0950.
"""

import random

number = []
attempts = 0


# Makes random 4 digit number
def _MakeNumber():
    for _i in range(4):
        x = random.randrange(0, 9)
        number.append(x)
    # If there are repeating numbers, start loop again
    if len(number) > len(set(number)):
        number.clear()
        _MakeNumber()


# Start game loop
def _PlayGame():
    global attempts
    attempts += 1
    numbers_correct = 0
    places_correct = 0
    # print(number)

    # User input loop for error checking
    while True:
        choice = input("Please enter a 4 digit number:")

        if not choice.isdigit():
            print("Non-digit found, try again.")
            continue

        digits = set(choice)
        if len(digits) != len(choice):
            print("You had repeated digits, try again.")
            continue

        if len(choice) != 4:
            print("Your input must be 4 digits long, try again.")
            continue
        break
    # Lose condition and message
    if attempts >= 12:
        print(f"Sorry, you lost! The answer was {number}!")
    # If lose condition is not met, go here to start evaluation checks
    else:
        guess = []
        # Write user input "choice" into list variable "guess"
        for i in range(4):
            guess.append(int(choice[i]))
        # Compares list "guess" to list "number" which is the answer. Adds
# the number of correct numbers in correct spot to numbers_correct
# variable
        for i in range(4):
            for j in range(4):
                if guess[i] == number[j]:
                    numbers_correct += 1
        # Compares list "guess" to list "number" which is the answer. Adds
# the number of correct numbers to places_correct variable
        for x in range(4):
            if guess[x] == number[x]:
                places_correct += 1
        print(f"Your guess has {places_correct} correct numbers in the\
 correct spot.")
        print(f"Your guess has {numbers_correct} numbers correct.")
        print(f"You have made {attempts} guesses.")
        # Win condition and message
        if places_correct == 4:
            print(f"You won after {attempts} attempts!")
        # If no win condition exists, start game loop again.
        elif places_correct != 4:
            _PlayGame()


_MakeNumber()
_PlayGame()
