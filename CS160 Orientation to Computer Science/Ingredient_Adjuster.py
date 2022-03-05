# Ingredient Adjuster by Brady Esplin
# I have taken each of the base ingredients and divided them by 48 which should
# give me the amount of ingredient per cookie. We shall see if I am correct.

sugar = .03125
butter = .02083333333333333332
flour = .057291666666666666664

number_cookies = int(input("How many cookies do you want to make?"))

output_sugar = sugar*number_cookies
output_butter = butter*number_cookies
output_flour = flour*number_cookies

print("The number of cups of ingredients you need to use are as follows:")
print("Sugar")
print (format(output_sugar, ".2f"))
print("Butter")
print (format(output_butter, ".2f"))
print("Flour")
print (format(output_flour, ".2f"))



