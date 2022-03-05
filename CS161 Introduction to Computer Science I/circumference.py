# Brady Esplin CS161 MWF 0800-0950 Circumference Exercise
# calculate area and circumference of circle from radius
# Step 1 Prompt for radius
# Step 2 apply the area formula
# Step 3 Print results 
 
import math

radius_str = input("Enter the radius of your circle:")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print ("The circumference is:",circumference,"\
    , and the area is:",area)
