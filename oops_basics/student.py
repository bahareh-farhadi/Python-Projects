class student:
    
    #this is a 'static'/'instance' method
    major='csc'
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
s1=student(1,'john')
s2=student(2,'bill')
print(s1.major,s2.major,s1.name,s2.name)