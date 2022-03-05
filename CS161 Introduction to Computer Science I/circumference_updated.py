"""Calculate area and circumference of circle from radius""" # This is a docstring. It should tell everyone what this program is and what it does.
# Brady Esplin CS161 MWF 0800-0950 Circumference Exercise
# Step 1 Prompt for radius
# Step 2 apply the area formula
# Step 3 Print results 
 
import math # imports math library and functions

radius_str = input("Enter the radius of your circle:") # asks user for input about radius of circle
radius_int = int(radius_str) # converts the user-entered string to a integer

circumference = 2 * math.pi * radius_int # calculates circumference
area = math.pi * (radius_int ** 2) # calculates area

print(f"The circumference is: {circumference}, and the area is {area}") #This is an f-string, tells 
# python that what follows is a formatted string. Python looks for curly braces, knows it is a placeholder, looks for variable.

#print ("The circumference is:",circumference,"\
#    , and the area is:",area)
