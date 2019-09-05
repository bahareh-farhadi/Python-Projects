from tkinter import PhotoImage

#JSON gives us live data info from the Internet
import json
import turtle
import urllib.request
import time

#this links display some information about the ISS(i.e. people,etc) in the form of a list of dictionaries
url="http://api.open-notify.org/astros.json"

#call the web service
response=urllib.request.urlopen(url)

#load the json response into a data structure(result)
result=json.loads(response.read())
print(result)

#access the values from the dictionary
print('Number of people in space=',result['number'])

#create a dictionary with info of the people
people=result['people']
for i in people:
  print(i)
  print(i['name'],'in',i['craft'])
  
#this link provides info on the position of the spaceship and timestamp in the form of a list of dictionaries
ship_url="http://api.open-notify.org/iss-now.json"
ship_response=urllib.request.urlopen(ship_url)
ship_res=json.loads(ship_response.read())
print(ship_res)

#access latitude and longitude values through the dictionary and convert them 
#from string type variables to floating point type numbers
lat=float(ship_res['iss_position']['latitude'])
print('latitude=',lat)
lon=float(ship_res['iss_position']['longitude'])
print('longitude=',lon)

#we can show the spaceship on the planet earth on a turtle screen
screen=turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)

#the background picture is a picture of the Earth from NASA
screen.bgpic(r"nasa.gif")

#register the spaceship's picture to the screen
screen.register_shape(r'16462.gif')
iss=turtle.Turtle()
iss.shape(r'16462.gif')
iss.setheading(90)
iss.penup()
iss.goto(lon,lat)

location=turtle.Turtle()
location.color('Yellow')
location.penup()
location.goto(-95.097,29.5502)
location.pendown()
location.dot(7)
location.hideturtle()

#the url is originaly http://api.open-notify.org/iss-pass.json, but since 
#it gets lat and lon as inputs, we have to add them to the url in our declaration
#this link provides time at any specified location given latitude and longitude of that location on the Earth
location_url="http://api.open-notify.org/iss-pass.json?lat=29.5502&lon=-95.097"
location_response=urllib.request.urlopen(location_url)
location_result=json.loads(location_response.read())
print(location_result)
print('pass over time at the location (lon,lat)=(-95.097,29.5502)',location_result['response'][1]['risetime'])
style=('Arial',10,'bold')

#time is given in a number, so we use time.ctime() in order to convert it to a readable time
location.write(time.ctime(location_result['response'][1]['risetime']),font=style)
screen.mainloop()