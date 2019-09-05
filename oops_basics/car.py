class car:
    def __init__(self,make,year):
        self.make=make
        self.year=year
    class engine:
        def __init__(self,number):
            self.number=number
        def started(self):
            print('engine started')
#this creates an instance of the outer class
c=car('bmw',2017)

#creates an instance of the inner class
e=c.engine(1234)

#invokes a method of the inner class
e.started()
