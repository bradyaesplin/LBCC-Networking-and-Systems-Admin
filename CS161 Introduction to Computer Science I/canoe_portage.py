"""Canoe Portage Solution for CS161 MWF 0800-0950."""
# by Brady Esplin
# This program will ask for input from the user in the measurement
# "rods". The program will reprint that input and also convert and
# include the following measurements: Meters, Furlongs, miles, feet,
# and the time to walk the imput distance.

rods = input("How many rods do you have to walk?")  # Program takes input in
# form 'string' from user in measurement 'rods'.
RODS = float(rods)  # Converts the 'string' input to type 'float'

# print(type(RODS))  # Confirmed here that 'RODS' variable was
# converted to float.

METERS = RODS * 5.0292  # Converted rods to meters 1 rod = 5.0292 m
FURLONGS = RODS / 40  # Converted rods to furlongs 1 furlong = 40 rods
MILES = METERS / 1609.34  # Converted meters to miles 1 mile = 1609.34 m
FEET = METERS / 0.348  # Converted meters to feet 1 foot = 0.3048 m
WALK_TIME = MILES / 3.1  # Converted miles to walk speed, average
# speed being 3.1 mph

print("You have input:", (RODS), "rods.")  # Prints feedback to user
print("This is:", (FEET), "feet.")  # Prints feedback to user
print("This is:", (METERS), "meters.")  # Prints feedback to user
print("This is:", (FURLONGS), "furlongs.")  # Prints feedback to user
print("This is:", (MILES), "miles.")  # Prints feedback to user
print("It will take an average of", (WALK_TIME), "hours to walk this distance.")
# Prints the estimated walk time to the user in hours
