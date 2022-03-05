"""Fib.py Print user selection from Fibonacci Sequence.

by Brady Esplin for CS 161 MWF 0800-0900. Program prints the first N
numbers of the Fibonacci Sequence, or just that specific number in
the Fibonnaci Sequence, depending on user selection.
"""


def _output_to(USER_NUMBER):
    """Print numbers up to the specified number in the Fibonacci Sequence."""
    # First two numbers in sequence
    NUMBER_1 = 0
    NUMBER_2 = 1
    # Fibonacci Sequence Counter
    COUNT = 0
    # Sets start condition for loops

    if USER_NUMBER == 1:
        print(f" Fibonacci Sequence up to {USER_NUMBER}.")
        print(NUMBER_1)
    else:
        print(f"Fibonacci Sequence up to {USER_NUMBER}.")
        while COUNT < USER_NUMBER:
            print(NUMBER_1)
            CALCULATION = NUMBER_1 + NUMBER_2
            NUMBER_1 = NUMBER_2
            NUMBER_2 = CALCULATION
            COUNT += 1


def _output_number(USER_NUMBER):
    """Print the specified number in Fibonacci Sequence."""
    # First two numbers in sequence
    NUMBER_1 = 0
    NUMBER_2 = 1
    # Fibonacci Sequence Counter
    COUNT = 0
    # Sets start condition for loops

    if USER_NUMBER == 1:
        print(f" Fibonacci Sequence Number: {USER_NUMBER}.")
        print(NUMBER_1)
    else:
        print(f"Fibonacci Sequence Number: {USER_NUMBER}.")
        while COUNT < USER_NUMBER:
            CALCULATION = NUMBER_1 + NUMBER_2
            NUMBER_1 = NUMBER_2
            NUMBER_2 = CALCULATION
            COUNT += 1
            if COUNT == USER_NUMBER:
                print(NUMBER_1)


# Program Starts Here
COUNT = 0

while COUNT == 0:
    USER_SELECTION = int(input("Would you like to print all the numbers\
 up to and including your number, or just your number? Select 1 for all\
 the numbers or select 2 for just your number. Then press ENTER:"))

    if USER_SELECTION == 1:

        USER_NUMBER = input("What number would you like to print up to\
 and include? (positive numbers only!): ")

        if USER_NUMBER.isdigit:
            USER_NUMBER = int(USER_NUMBER)
            _output_to(USER_NUMBER)
            COUNT += 1
        else:
            print("Please enter a valid number!")

    elif USER_SELECTION == 2:

        USER_NUMBER = input("What number of the sequence would you like\
 me to print out? (positive numbers only!): ")

        if USER_NUMBER.isdigit:
            USER_NUMBER = int(USER_NUMBER)
            _output_number(USER_NUMBER)
            COUNT += 1
        else:
            print("Please enter a valid number!")

    elif USER_SELECTION != 1 or 2:
        print("That was not a valid selection, try again!")
        continue
