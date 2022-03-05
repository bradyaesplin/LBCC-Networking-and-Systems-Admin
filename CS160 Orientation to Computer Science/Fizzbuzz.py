#Quinn Aschoff & Brady Esplin

for x in range(1, 51): #Defining the range of x values for printing. 
    if x % 3 == 0 and x % 5 ==0 :
        print("FizzBuzz") #So for these two lines it's checking if the value is divisible by 3 and5 and putting that at a higher priority than if it was divisible by only one of them to print FizzBuzz

    elif x % 3 == 0: 
        print("Fizz") #If the number is divisible by 3 and not by 5 then print Fizz

    elif x % 5 == 0:
        print("Buzz") #If the number is divisible by 5 and not by 3 then print Buzz
        
    else: 
        print (x) #If the number is divisible by neither 3 or 5 (Nor both) simply print the number itself. 
