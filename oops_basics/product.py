class product():
    
    #this is a method of the class
    def __init__(self):
        
        #name, description and price are the fields of this class
        self.name='iPhone'
        self.description='great'
        self.price=1000
    
        
#this creates an object
p1=product()

#we are accessing the object's fields 
print(p1.name,'\t',p1.description,'\t',p1.price)

    