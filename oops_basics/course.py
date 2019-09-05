from test.test_iter import IteratingSequenceClass
class Course:
    
    #name and ratings are the parameters that are going to be passed into the object
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
        
    #this is called an 'instance method'
    def average(self):
        number_of_ratings=len(self.ratings)
        average=sum(self.ratings)/number_of_ratings
        return average
c1=Course('john',[1,2,3,4,5])
print(c1.name,'\t',c1.ratings,'\t',c1.average())

