"""Persistence.py for Lab 3, CS161 MWF 0800-0950."""
# by Brady Esplin
# Program will take user input of integer and check for negative numbers.
# Program will sum the digits of said integer until single digit reached.
# Program will display the additive persistence of integer and additive
# root of integer.
# Program will find the products of the digits of said integer until a
# single digit reached.
# Program will display the multiplicative persistence of integer and
# multiplicative root of integer.
# Program will continue until user quits.

# Describes program to user, takes user input and assigns it to variable
print("If you input an integer I can tell you the additive and multiplicative\
 persistence and the additive and multiplicative root!")

# Sets variable equal to 1 to check for negative neumbers in loop below
USER_INPUT = 1

# Gets actual user input
USER_INPUT = input("What number would you like to use? Type it and press ENTER.\
(Negative integer to exit)")

# Convers input to integet to compare to 0 for loop below
USER_INPUT = int(USER_INPUT)

if USER_INPUT > 0:
    # Error checking previous code
    print(f"For the integer: {USER_INPUT}")
    USER_INPUT = str(USER_INPUT)

    # I had to duplicate the user input into two different variables as having
    # only one variable was causing the program to throw an error. I believe
    # it was due to the user input being changed in the first set of loops.
    USER_INPUT_1 = USER_INPUT
    USER_INPUT_2 = USER_INPUT

    # Additive persistence variable = 0, to set up loop count
    A_PERS = 0

    # Tells loop to continue looping until the user input is reduced to the
    # length of 1
    while len(USER_INPUT_1) > 1:
        # Sets answer to starting value of zero
        SUM_1 = 0
        # Sets loop to run for every element from the user input
        for element in USER_INPUT_1:
            # Answer equals starting value of answer plus the element
            # converted to an integer, repeats until there are no more
            # elements left
            SUM_1 += int(element)
            # Error checking loop operations
            # print(f" The sum is {SUM_1}")
        # Converts answer back to string to be measured for length, will exit
        # loop if less than 2 elements remain
        USER_INPUT_1 = str(SUM_1)
        # Counts iterations of loop to calculate the additive persistence
        A_PERS += 1

    # Displays the final answer and loop count to user
    print(f"Additive root is {SUM_1}, Additive persistence is {A_PERS}")

    # Multiplicative persistence variable = 0, to set up loop count
    M_PERS = 0

    # Tells loop to continue looping until the user input is reduced to the
    # length of 1
    while len(USER_INPUT_2) > 1:
        # Sets answer to starting value of one
        ANSWER = 1
        # Sets loop to run for every element from the user input
        for element in USER_INPUT_2:
            # Answer equals starting value of answer times the element
            # converted to an integer, repeats until there are no more
            # elements left
            ANSWER *= int(element)
            # Error checking loop operations
            # print(f" The product is {ANSWER}")
        # Converts answer back to string to be measured for length, will exit
        # loop if less than 2 elements remain
        USER_INPUT_2 = str(ANSWER)
        # Counts iterations of loop to calculate the additive persistence
        M_PERS += 1

    # Displays the final answer  and loop count to user
    print(f"Multiplicative root is {ANSWER}, Multipicative persistence is {M_PERS}")
else:
    print("Input value is negative, Goodbye!")
    raise SystemExit
