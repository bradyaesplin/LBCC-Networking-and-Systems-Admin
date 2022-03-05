# Number Guessing Game by Quinn Aschoff and Brady Esplin

import random 

print("Hi! I am thinking of a number between 1 and 100, try to guess it!") #introduction

computer_number = False #sets the very beginning of the loop so the computer can pick another
                        #number once the previous number has been guessed

while computer_number == False: #lets computer pick a random number
    
    computer_number = random.randint(2,101) #sets computer number to be random integer

    user_number = False #sets user input to be false allowing above code to run.

    while user_number == False: #sets code to loop/restart when there is no user number in play

        while True: #once user gives input, loops input through this loop
        
            try:
                user_number = int(input("What number am I thinking of?")) #first user input, starts loop

            except ValueError:
                print("That doesn't sound like an answer I can use!") #error catcher

            else: #if no error will break out of this loop and move on to giving feedback
                break
    
        if computer_number == user_number: #win condition 
            print("Good job, you got it! I am going to think of another number for you to guess!")
            computer_number = False #tells computer to pick a new random number
            break #sends program back to error checking loop
            
        if computer_number > user_number: #indicates that the user number is lower than the computer number
            print("Nope! Too low! Try again.")

        if computer_number < user_number: #indicates that the user number is higher than the computer number
            print("Ha! No, too high. Guess again.")

        user_number = False #resets loop, generating a new computer number for the user to guess

                  

