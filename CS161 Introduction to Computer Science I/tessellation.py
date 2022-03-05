"""Tesselation.py Draw Tesselation with User Input.

by Brady Esplin for CS161 MWF 0800-0950. Program will be made up of a
minimum of three functions. Will use turtle to draw a tesselation of
hexagons.
"""


import math
# Found on stackoverflow as a workaround for the pylint errors
from turtle import Screen, Turtle
screen = Screen()
turtle = Turtle()


# Function to get color_choice
def _get_color_choice():
    """Return color choice from user in (str) form."""
    print(" What color would you like to use? The colors that you\
 have available are:")
# List of available colors for error checking
    AVAILABLE_COLORS = ["white", "black", "blue", "cyan", "green",
                        "yellow", "brown", "orange", "red"]
    # Prints list so user can see choices
    for x in AVAILABLE_COLORS:
        print(x)
    # Runs error checking loop until legal color chosen
    while True:
        color_choice = input("What would you like your color to be?")
        if color_choice in AVAILABLE_COLORS:
            break
        print("You must pick from the available colors!")
        continue

    return color_choice


# Function to get num_hex
def _get_num_hexagons():
    """Return number choice from user in (int) form."""
    # Starts error checking loop
    while True:
        num_hex = int(input("How many hexagons per row? (4-20):"))
        if 4 <= num_hex <= 20:
            break
        print("You must choose a number between 4 and 20!")
        continue

    return num_hex


def _draw_hexagon(x, y, side_len, turtle, color):
    """Draw and fill hexagon."""
    # Draw and fill hexagon
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)

    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)

    turtle.end_fill()
    turtle.penup()


print("Hello User! I will draw a pattern of hexagons based on your input!")

# Calls function and writes to
COLOR_1 = _get_color_choice()
COLOR_2 = _get_color_choice()

# Calls function and writes to
NUM_HEX = _get_num_hexagons()

# Finds width of hexagon (d) given NUM_HEX
HEX_WIDTH = 500/NUM_HEX

# Calculates incircle radius length
INCIRCLE_RADIUS = HEX_WIDTH / 2

# Sets up horizontal offsetting each row
H_OFFSET = 0

# Sets up vertical offsetting each row
V_OFFSET = INCIRCLE_RADIUS * 1.75

# Total start position calculation
START_POSTION = - (NUM_HEX * HEX_WIDTH / 2), - (NUM_HEX * HEX_WIDTH / 2)

# Gives feedback to me
print(f"You chose {COLOR_1} and {COLOR_2}!")
print(f"You chose to have {NUM_HEX} hexagons per row!")
print(f"Your start position is {START_POSTION}!")
print(f"Your Hexagon width is {HEX_WIDTH}!")

# Positions turtle to start tessellation
turtle.speed(0)
turtle.penup()
turtle.left(150)

for y in range(NUM_HEX):
    if y % 2 == 0:
        H_OFFSET = INCIRCLE_RADIUS * 0.5
    else:
        H_OFFSET = -(INCIRCLE_RADIUS * 0.5)
    for x in range(NUM_HEX):
        if x % 2 == 0:
            color = COLOR_1
        else:
            color = COLOR_2
        _draw_hexagon(
            # x value
            (HEX_WIDTH * x) + H_OFFSET - (NUM_HEX * HEX_WIDTH / 2),
            # y value
            (V_OFFSET * y) + (V_OFFSET / 6) - (NUM_HEX * HEX_WIDTH / 2),
            # side length
            HEX_WIDTH / math.sqrt(3),
            # turtle
            turtle,
            # color
            color
        )

screen.exitonclick()
