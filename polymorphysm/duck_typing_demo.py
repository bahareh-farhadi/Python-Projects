'''this piece of code shows the basic idea of polymorphism:
you can see that we pass objects of different classes(duck and human) 
at run-time to the same function, and it performs different behaviors based on 
the object type. This is called polymorphism(multi-behavior)'''
class duck:
    def talk(self):
        print('quack quack')
class human:
    def talk(self):
        print('hello')
def call_talk(obj):
    obj.talk()
d=duck()
call_talk(d)
h=human()
call_talk(h)