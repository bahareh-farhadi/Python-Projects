#import the modules
from turtle import *
from random import randint
from unittest.mock import right

#this function sets random r,g,b color codes to a given shape
def random_color(shape):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    shape.color(r,g,b)

#this function sets a given shape's position with random x,y coordinates
def random_position(shape):
    x=randint(-100,100)
    y=randint(-100,100)
    shape.penup()
    shape.goto(x,y)
    shape.pendown()

#this function sets random heading angle to a given shape
def random_heading(shape):
    angle=randint(0,360)
    shape.setheading(angle)
    #OR
    #shape.right(angle)

#this function draws a rectangle of a random color, at a random position
#and with random height and widht (uses the above functions) 
def draw_rectangle():
    rect=Turtle()
    rect.hideturtle()
    
    #speed(0) makes turtle draw at its fastest
    rect.speed(0)
    
    #use the above functions to set random color and position
    random_color(rect)
    random_position(rect)
    
    #generate random height and width numbers using the randint function
    height=randint(10,100)
    width=randint(10,100)
    
    #begin_fill allows to draw a filled shape
    rect.begin_fill()
    rect.forward(width)
    rect.right(90)
    rect.forward(height)
    rect.right(90)
    rect.forward(width)
    rect.right(90)
    rect.forward(height)
    rect.right(90)
    rect.end_fill()

#this function draws circles
def draw_circle():
    screen.colormode(255)
    circ=Turtle()
    circ.hideturtle()
    circ.speed(0)
    random_color(circ)
    random_position(circ)
    diameter=randint(20,100)
    
    #dot draws a filled circle with a given diameter
    circ.dot(diameter)
    
#this function is very similar to draw_rectangle function with the only difference
#that the angles at which the turtle's heading changes are different in order to
#draw stars
def draw_stars():
    screen.colormode(255)
    star=Turtle()
    star.hideturtle()
    star.speed(0)
    random_color(star)
    random_position(star)
    star.begin_fill()
    side_len=randint(10,80)
    star.right(72)
    star.forward(side_len)
    
    star.left(72)
    star.forward(side_len)
    
    star.right(144)
    star.forward(side_len)
    
    star.left(72)
    star.forward(side_len)
    
    star.right(144)
    star.forward(side_len)
    
    star.left(72)
    star.forward(side_len)
    
    star.right(144)
    star.forward(side_len)
    
    star.left(72)
    star.forward(side_len)
    
    star.right(144)
    star.forward(side_len)
    
    star.left(72)
    star.forward(side_len)
    star.end_fill()
        
        

    
    
        
screen=Screen()
screen.bgcolor('white')
turtle=Turtle()
turtle.shape('turtle')
screen.colormode(255)
turtle.speed(10)

#draw 30 turtles 
for i in range(30):
    random_color(turtle)
    random_position(turtle)
    random_heading(turtle)
    turtle.stamp()
screen.clear() 
turtle=Turtle()
turtle.shape('turtle')
screen.colormode(255)
random_color(turtle)
turtle.setheading(0)

#draw 30 of each shape and clear the screen once switching to a new shape
for i in range(30):
    draw_rectangle()
screen.clear()
for i in range(30):
    draw_circle()
screen.clear()
for i in range(30):
    draw_stars()
screen.mainloop()

