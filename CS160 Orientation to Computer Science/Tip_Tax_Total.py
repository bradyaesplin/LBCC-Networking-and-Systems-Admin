# Tip Tax Total by Brady Esplin

mealCost = float(input("What is the cost of your meal?"))

tipCost = 0.18
meal_and_tip = mealCost*tipCost
print ("Your tip today is")
print (meal_and_tip)

taxCost = 0.07
meal_and_tax = mealCost*taxCost
print ("Your tax today comes to")
print (meal_and_tax)

totalCost = meal_and_tip+meal_and_tax+mealCost
print ("Your total cost today is")
print (totalCost)


                  
