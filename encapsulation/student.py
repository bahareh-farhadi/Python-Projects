from ctypes.test.test_pickling import name
class student:
    def __init__(self):
        self.__id=123
        self.__name='john'
    def display(self):
        print(self.__id,'\t',self.__name)
        
s=student()

''' so initially, you can see that id and name are not private, and are 
 even accessible outside the class 
so if we add __ to the beginning of id and name, they become private and 
we cannot access them outside the class.
Now if you want to access them, you can define a function inside the class and
simply print the values,
but if you want to use the variables besides printing them,
you can use: s._student__id,
the reason why we can access these private fields is that they are not completely private,
but they are HIDDEN, and are accessible like so, this is called NAME MANGLING'''
s.display()
print(s._student__id)
print(s._student__name)


'''another way to do this is to define setter and getter functions inside the class'''
class student1:
    
    #we need the @reserved... because id is used for some other stuff, so we need it to prevent any errors
    def set_id(self,id):  # @ReservedAssignment
        self.id=id
    def get_id(self):
        return self.id
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
s1=student1()
s1.set_id(2)
s1.set_name('bahar')
print(s1.get_id(),'\t',s1.get_name())

