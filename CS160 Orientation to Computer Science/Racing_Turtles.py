# Turtle Race by Brady Esplin

from turtle import * #imports turtles
from random import randint #allows use of random integer

speed(0) #makes my arrow turtle set up the racetrack fast
penup() #arrow turtle picks up pen
goto(-140,140) #goes to where I want my track located on the Cartesian Plane

for step in range(16): #use 16 steps to repeat this loop 15 times
    write(step, align='center') #write distance markers and align
    right(90) #turn 90 degrees to face "east"
    forward(10) #move forward 10 pixels
    pendown() #pen down, prepare to write
    forward(150) #move forward 150 pixels, writing
    penup() #pick up pen
    backward(160) # go back north to "top" of track
    left(90) #turn left 90 degrees to face east
    forward(20) #move forward 20 pixels to start of where I want the next line and number to start

right(90) #when done drawing track, arrow turtle will standby to judge the results

red_turtle = Turtle() #defines this turtle, names it
red_turtle.color('red') #defines the color
red_turtle.shape('turtle') #defines the shape

red_turtle.penup() #pick up pen, don't draw
red_turtle.goto(-160, 100) #move to starting line
red_turtle.pendown() #pen down, ready to start

blue_turtle = Turtle() #defines this turtle, names it
blue_turtle.color('blue') #defines the color
blue_turtle.shape('turtle') #defines the shape

blue_turtle.penup() #pick up pen, don't draw
blue_turtle.goto(-160, 70) #move to starting line
blue_turtle.pendown() #pen down, ready to start

green_turtle = Turtle() #defines this turtle, names it
green_turtle.color('green') #defines the color
green_turtle.shape('turtle') #defines the shape

green_turtle.penup() #pick up pen, don't draw
green_turtle.goto(-160, 40) #move to starting line
green_turtle.pendown() #pen down, ready to start

yellow_turtle = Turtle() #defines this turtle, names it
yellow_turtle.color('yellow') #defines the color
yellow_turtle.shape('turtle') #defines the shape

yellow_turtle.penup() #pick up pen, don't draw
yellow_turtle.goto(-160, 10) #move to starting line
yellow_turtle.pendown()#pen down, ready to start

for turn in range(105): #use 105 steps to repeat this loop 104 times
    red_turtle.forward(randint(1,5)) #move forward a random number of pixels (1-5)
    blue_turtle.forward(randint(1,5)) #move forward a random number of pixels (1-5)
    green_turtle.forward(randint(1,5)) #move forward a random number of pixels (1-5)
    yellow_turtle.forward(randint(1,5)) #move forward a random number of pixels (1-5)
