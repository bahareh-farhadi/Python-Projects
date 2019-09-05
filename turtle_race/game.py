#imports all methods from the module 'turtle'
from turtle import *
from random import randint
mouse=Turtle()
mouse.speed(0)
mouse.penup()
mouse.goto(-140,140)
print(window_width())
for i in range(16):
    if i==15:
        last_x_cor=mouse.xcor()
    mouse.write(i,align='center')
    mouse.right(90)
    mouse.forward(10)
    for i in range(10):
        mouse.pendown()
        mouse.forward(15)
        mouse.penup()
        mouse.forward(10)
    mouse.penup()
    mouse.backward(260)
    mouse.left(90)
    mouse.forward(20)
  
print(last_x_cor)
#TURTLE 1
turtle1=Turtle()
turtle1.color('red')
turtle1.shape('turtle')
turtle1.penup()
turtle1.goto(-160,100)
for i in range(36):
  turtle1.right(10)
turtle1.pendown()

#TURTLE 2
turtle2=Turtle()
turtle2.color('blue')
turtle2.shape('turtle')
turtle2.penup()
turtle2.goto(-160,50)
for i in range(36):
  turtle2.right(10)
turtle2.pendown()

#TURTLE 3
turtle3=Turtle()
turtle3.color('green')
turtle3.shape('turtle')
turtle3.penup()
turtle3.goto(-160,0)
for i in range(36):
  turtle3.right(10)
turtle3.pendown()

#TURTLE 4  
turtle4=Turtle()
turtle4.color('yellow')
turtle4.shape('turtle')
turtle4.penup()
turtle4.goto(-160,-50)
for i in range(36):
    turtle4.right(10)
turtle4.pendown()

for i in range(120):
    turtle1.forward(randint(1,7))
    turtle2.forward(randint(1,7))
    turtle3.forward(randint(1,7))
    turtle4.forward(randint(1,7))
    max_x=max(turtle1.xcor(),turtle2.xcor(),turtle3.xcor(),turtle4.xcor())
    if max_x>=last_x_cor:
        if max_x==turtle1.xcor():
            print('RED turlte wins')
        elif max_x==turtle2.xcor():
            print('BLUE turlte wins')
        if max_x==turtle3.xcor():
            print('GREEN turlte wins')
        if max_x==turtle4.xcor():
            print('YELLOW turlte wins')
        break
  


  
