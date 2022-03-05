# this string is what we would call a 'string literal' - its value is LITERALLY
# part of the program's code It would be preferable to use a variable
# to store the parts of code you expect to change.

# print("Hello Brady")

# The code below is more flexible because we use a variable to hold the
# name and we can re-use that variable whenever we need to print the user's name.
#
# name = "Brady" # creates a variable called "name" and sets its value to "Brady"
# print("Hello" , name) # use the variable in our greeting
# print("... here we are doing lots of interesting work together...")
# print("Goodnight,", name) 

# Here we us Python's input() function to ask the user for thier name.
#
# creates a variable called "name" and sets its value to what is returned
# by the input() function

name = input("Please enter your name: ")
#print("Hello" , name, "!") # use the variable in our greeting
print(f"Hello, {name}!") # <--- format string
print("... here we are doing lots of interesting work together...")
print("Goodnight,", name)
print(f"don't let the bedbugs bite!")





