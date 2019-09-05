class flight:
    def __init__(self,engine):
        
        '''so here we are introducing the field engine to this class,
        this is called "dependency injection"
        and then we can pass ANY type of object as "engine",
        if it's an "airbus" engine, the method from the respective class is invoked,
        and if a "boeing" engine is passes, the start function from the "boeing_engine"
        class is invoked;
        is this case he start_engine method is POLYMORPHIC,
        since it has multiple behaviors depending on its parameters'''
        self.engine=engine
    def start_engine(self):
        self.engine.start()
class airbus_engine:
    def start(self):
        print('starting airbus engine')
class boeing_engine:
    def start(self):
        print('starting boeing engine')
ae=airbus_engine()
f=flight(ae)
f.start_engine()
be=boeing_engine()
f1=flight(be)
f1.start_engine()