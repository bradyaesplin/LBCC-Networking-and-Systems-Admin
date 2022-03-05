#Quinn Aschoff, Brady Esplin

from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]
player = False 

wins = 0
losses = 0

while player == False:
     player = input("Rock, Paper, Scissors?")
     
     if player == computer:
           print ("Tie!")
     elif player =="Rock" :
          if computer == "Paper" :
              print ("You lose!", computer, "covers", player)
              losses += 1
              
          else:
              print ("You win!", player, "smashes", computer)
              wins += 1
              
     elif player == "Paper":
         if computer == "Scissors":
              print ("You lose!", computer, "cut", player)
              losses += 1
              
         else:
               print ("You win!", player, "covers", computer)
               wins += 1
               
     elif player == "Scissors":
         if computer == "Rock":
             print ("You lose....", computer, "smashes", player)
             losses += 1
         else:
             print ("You win!", player, "cut", computer)
             wins += 1
     else:
          print ("That's not a valid play. Check your spelling!")

     print ("You have won", wins, "games and lost", losses, "games")


     
     again=str(input("Do you want to play again, type yes or no  "))
     if again =="no":
          exit ()
               
     
     
     player = False

     computer = t[randint(0,2)]

    
        
    
                                    
