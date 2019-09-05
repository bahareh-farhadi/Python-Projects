import pygal

#create a new pie chart using the function from the pygal module
piechart=pygal.Pie()
piechart.title='Favorite Colors'

#similar to pie chart, we could create a bar chart like so
bargraph=pygal.Bar()
bargraph.title='Favorite Colors'

#the text file includes color names and number of people who like the respective colors
file=open('survey_information.txt','r')

#loop through each line in the file separately 
for line in file.read().splitlines():
  
  #if there's an empty line at the end of the file, this will
  #take care of it, otherwise we'll get an error
  if line:
      
    #split colors and numbers with the space
    (color,num)=line.split(' ')
    
    #use int(num), because when numbers are stored from the text file
    #they are saved as string type variables initially.
    piechart.add(color,int(num))
    bargraph.add(color,int(num))

#render displays the charts
piechart.render()
bargraph.render()