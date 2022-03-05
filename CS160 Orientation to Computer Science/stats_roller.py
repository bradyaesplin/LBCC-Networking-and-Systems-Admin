# RPG Stats Roller by Quinn Aschoff and Brady Esplin

import random

stat_list = [] #defines empty stat list

for stat in range(6): #starts a loop for 6 iterations

    dice_number_1 = random.randint(1,6) #import random integer from 1-6, to stand in for roll of dice
    dice_number_2 = random.randint(1,6) #import random integer from 1-6, to stand in for roll of dice
    dice_number_3 = random.randint(1,6) #import random integer from 1-6, to stand in for roll of dice
    dice_number_4 = random.randint(1,6) #import random integer from 1-6, to stand in for roll of dice

    dice_roll = [dice_number_1, dice_number_2, dice_number_3, dice_number_4] #makes list of dice rolls into one number
    dice_roll.remove(min(dice_roll)) #removes the smallest number from the list

    list_rolls = (sum(dice_roll)) #adds the remaining numbers together
    stat_list.append(list_rolls)    #adds that number to our empty list

sorted_stat_list= sorted(stat_list) #sorts those numbers into a new variable
sorted_stat_list.reverse() #makes this list show up from greatest to smallest
print(sorted_stat_list) #display that list to the user
