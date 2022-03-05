"""Hertz Conversions from user input octave and pitch class."""
# By Brady Esplin for CS161 MWF 0800-0950
# This program will take three octave and pitch classes from the user,
# convert them to HZ, and play them using the Beep function from
# Windows. Reference tone is 4.9, which is A in the 4th octave, 440 Hz
# formula used to convert is UserHz = 440 * 2 to the power of
# ((UserOctave-4) + (UserPitchClass-9 / 12)

print("Hello! This program can take note octave and pitch classes from you in \
the form of numbers and convert them to Hertz, displaying these properties \
for you. Lets get started!")
# explains program to user

user_octave_one = input("What is your first octave? Type it and press enter.")
# takes input from user, assigns to variable
user_pitchclass_one = input("What is your first pitch class? Type it and press enter.")
# takes input from user, assigns to variable

user_octave_one = int(user_octave_one)  # changes variable from str to int
user_pitchclass_one = int(user_pitchclass_one)  # changes variable from str to int

o_diff_one = (user_octave_one) - 4
# finds difference of octave, sets equal to variable o_diff_one
pc_diff_one = (user_pitchclass_one) - 9
# finds difference of pitch class, sets equal to variable pc_diff_one

user_power_one = ((o_diff_one) + ((pc_diff_one) / 12))
# calculates the power to use in the equation to find user_hz_one

user_hz_one = (440 * pow(2, (user_power_one)))
# calculates the users Hertz using the supplied formula
print(f"{user_octave_one}.{user_pitchclass_one} is {user_hz_one} Hertz")
# displays users input and the resulting Hertz

print("Lets do it again!")

user_octave_two = input("What is your next octave? Type it and press enter.")
# takes input from user, assigns to variable
user_pitchclass_two = input("What is your next pitch class? Type it and press enter.")
# takes input from user, assigns to variable

user_octave_two = int(user_octave_two)  # changes variable from str to int
user_pitchclass_two = int(user_pitchclass_two)  # changes variable from str to int

o_diff_two = (user_octave_two) - 4
# finds difference of octave, sets equal to variable o_diff_two
pc_diff_two = (user_pitchclass_two) - 9
# finds difference of pitch class, sets equal to variable pc_diff_two

user_power_two = ((o_diff_two) + ((pc_diff_two) / 12))
# calculates the power to use in the equation to find user_hz_two

user_hz_two = (440 * pow(2, (user_power_two)))
# calculates the users Hertz using the supplied formula
print(f"{user_octave_two}.{user_pitchclass_two} is {user_hz_two} Hertz")
# displays users input and the resulting Hertz

print("And one last time!")
user_octave_three = input("What is your last octave? Type it and press enter.")
# takes input from user, assigns to variable
user_pitchclass_three = input("What is your last pitch class? Type it and press enter.")
# takes input from user, assigns to variable

user_octave_three = int(user_octave_three)  # changes variable from str to int
user_pitchclass_three = int(user_pitchclass_three)  # changes variable from str to int

o_diff_three = (user_octave_three) - 4
# finds difference of octave, sets equal to variable o_diff_three
pc_diff_three = (user_pitchclass_three) - 9
# finds difference of pitch class, sets equal to variable pc_diff_three

user_power_three = ((o_diff_three) + ((pc_diff_three) / 12))
# calculates the power to use in the equation to find user_hz_three

user_hz_three = (440 * pow(2, (user_power_three)))
# calculates the users Hertz using the supplied formula
print(f"{user_octave_three}.{user_pitchclass_three} is {user_hz_three} Hertz")
# displays users input and the resulting Hertz

print("Thank you for using the program!")
