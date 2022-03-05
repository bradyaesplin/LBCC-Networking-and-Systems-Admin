# Planting Grapevines by Brady Esplin

print("Welcome! If you input the values requested, I can do computer magic and give you the number of grapevines that will fit in a row!")

length_row = int(input("In feet, what is the length of the row of grapevines?"))
end_post = int(input("In feet, what is the space used by an end-post assembly?"))
space_between = int(input("In feet, what is the distance in between the grapevines?"))

number_grapevines_in_row = ((length_row - (end_post * 2)) / space_between)

print("The number of grapevines that will fit in the indicated row is:")
print(number_grapevines_in_row)

print("Have a good day!")



