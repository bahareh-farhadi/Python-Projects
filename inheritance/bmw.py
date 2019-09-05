class bmw:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print('starting the car')
    def stop(self):
        print('stopping the car')
class three_series(bmw):
    def __init__(self,cruise_control_enabled,make,model,year):
        
        #three series is inherited from the class bmw, so we have to inherit all the
        #fields from bmw like so:
       # bmw.__init__(self, make, model, year)
        
        '''another way to inherit the fields of the parent class:'''
        super().__init__(make,model,year)
        self.cruise_control_enabled=cruise_control_enabled
        
    '''we can have functions w/ exactly same names in both parent and inherited classes,
    the function in the inherited class OVER WRITEs the one in the parent class, 
    so when the function is accessed through the inherited class, the overwritten one is run'''
    def stop(self):
        print('over written the functionality in the parent class')
        
    '''you can also inherit the functionality from the parent AND add your own stuff
    to the function, it is basically done using 'super()' '''
    def start(self):
        super().start()
        print('button start')
class five_series(bmw):
    def __init__(self,parking_assist_enabled,make,model,year):
        
        #three series is inherited from the class bmw, so we have to inherit all the
        #fields from bmw like so:
        bmw.__init__(self, make, model, year)
        self.parking_assist_enabled=parking_assist_enabled
three=three_series(True,'BMW','328i','2018')
five=five_series(True,'BMW','528i','2017')
print(three.cruise_control_enabled,'\t',three.make,'\t',three.model,'\t',three.year)

'''you can see how functionality is inherited from the parent class(bmw),
so all functions from the parent class are accessible through their inherited classes;
however, the inherited class' fields are not accessible through the parent class'''
three.start()
three.stop()


    