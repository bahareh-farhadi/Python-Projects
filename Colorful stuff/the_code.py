#importing all functions from turtle module
from turtle import *

#colors used are stored in a dictionary in a file
file=open('color_dictionary.txt','r')

#creates a dictionary, key:color name, value:color code(downloaded from trinket)
color_dict={}

#store each line of the file in a list
lst=file.read().splitlines()
for i in lst:
    
    #split each line with ' : ', so we can separate keys and values
    (key,val)=i.split(' : ')
    print(key,val)
    
    #add the value to the respective key in the dictionary
    color_dict[key]=val
print(color_dict)

#create a new screen
screen=Screen()

#set up the screen size
screen.setup(600,600)

#background color
screen.bgcolor(color_dict['light pink'])

#the same color will be used until the color is changed
color(color_dict['grey'])

#set the text style
style=('Arial',40,'bold')

#add a text to the screen
write('Hello',font=style,align='center')
penup()
right(90)
forward(40)
pendown()
color(color_dict['cherry'])

#allows us to display the screen for 3 seconds to the user
screen.delay(3000)
write('world',font=style,align='center')
screen.clear()
screen.bgcolor('light blue')
color(color_dict['grey'])

#draws a filled circle with the given diameter
dot(600)
color(color_dict['cherry'])
style=('Arial',20,'bold')
left(90)
write('Do not\ncompare yourself with anyone\nin this world,\nif you do so\nyou are\nINSULTING YOURSELF',font=style,align='center')
#mainloop() keeps the window open
screen.mainloop()