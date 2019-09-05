#!/bin/python3
from turtle import *
from random import choice
screen = Screen()
screen.bgcolor('White')
turtle = Turtle()
turtle.penup()
turtle.hideturtle()

# opens the file, 'r' means 'read only'
file = open('cards.txt', 'r')
robots = {}

#read the file's lines separately
for i in file.read().splitlines():
    
    #split the names and store them as string variables
    name, battery, intelligence, image = i.split(', ')
    
    #add to the dictionary
    robots[name] = [battery, intelligence, image]
    
    #add the shape to the screen
    screen.addshape(image)
file.close()
print('Robots:  rainbow, space, bird, jet, twoheads, dog, round, brains, tv, hair, shades, yellow  (or random)')

#infinite loop
while True:
    x = input('Choose a robot: ')
    
    #users can choose robots from a given list, or just let the program choose randomly
    if x in robots or x == 'random':
        if x == 'random':
            
            #randomly chooses from all the keys in the dictionary
            x = choice(list(robots.keys()))
            
        #print the info of the chosen robot from dictionary(print values)
        print(robots[x])
        style = ('Verdana', 14, 'bold')
        turtle.clear()
        turtle.hideturtle()
        turtle.goto(0, 100)
        
        #the 3rd value in the dictionary is the robot's image
        turtle.shape(robots[x][2])
        turtle.setheading(90)
        turtle.stamp()
        turtle.setheading(-90)
        turtle.forward(70)
        # text='Name: '+x+'\nBattery Life: '+robots[name][0]+'\nIntelligence: '+robots[name][1]
        text = 'Name: ' + x
        turtle.write(text, font=style, align='center')
        turtle.forward(25)
        text = 'Battery Life: ' + robots[x][0]
        turtle.write(text, font=style, align='center')
        turtle.forward(25)
        text = 'Intelligence: ' + robots[x][1]
        turtle.write(text, font=style, align='center')
        turtle.forward(25)   
    else:
        print("The robot chosen does not exist")

