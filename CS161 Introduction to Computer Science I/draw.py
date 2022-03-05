"""User Input Controlled Turtle Drawing."""
# by Brady Esplin for CS161 MWF 0800-0950
# Program will output a description of what the program does, prompting
# the user for input in the correct form, using this input to draw
# multiple shapes of multiple colors.

# pylint: disable=no-member

import turtle
import time
import random

print("Hello user! I will draw a fan of squares for you in different colors!")

NUMBER_SQUARES = 0  # sets loop number to 0
while NUMBER_SQUARES < 1 or NUMBER_SQUARES > 30:  # requires user input
    # for loop to continue
    try:
        NUMBER_SQUARES = int(input("Please choose a number of squares to draw\
 between 1 and 30."))  # sets variable equal to integer input number
    except ValueError:
        print("Please enter a valid number!")  # prints error message
        # if a string is input
print(f"You chose {NUMBER_SQUARES}!")  # prints chosen integer

LENGTH_SIDE = input("How many pixels should each side be? Choose a number\
 between 1 and 200 please.")  # user inputs how large squares are
if LENGTH_SIDE.isdigit():  # checks user input digit
    LENGTH_SIDE = int(LENGTH_SIDE)  # converts to integer
else:
    print("Please enter a valid number!")  # prints error message

if 1 < LENGTH_SIDE < 200:  # checks that length is in
    # designated range
    print(f"You chose {LENGTH_SIDE}")  # prints confirmation

SQUARE_ROTATION = 360 / (NUMBER_SQUARES)  # sets variable number to
# 360 dividedby user input number, should result in an even dispersment
# of squares.

turtle.speed(9)

for i in range(NUMBER_SQUARES):  # sets loop for user input number
    turtle.right(SQUARE_ROTATION)  # rotates pen
    turtle.color(random.random(), random.random(), random.random())
    # pen random color
    turtle.begin_fill()  # fills shape
    turtle.forward(150)  # draw side 1
    turtle.right(90)  # rotate
    turtle.forward(150)  # draw side 2
    turtle.right(90)  # rotate
    turtle.forward(150)  # draw side 3
    turtle.right(90)  # rotate
    turtle.forward(150)  # draw side 4
    turtle.right(90)  # rotate
    turtle.end_fill()  # stop filling shape

time.sleep(10)  # displays picture for 10 seconds
turtle.bye()  # dismisses turtle
