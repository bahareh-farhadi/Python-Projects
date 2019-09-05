class programmer:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_salary(self,sal):
        self.salary=sal
    def get_salary(self):
        return self.salary
    def set_technology(self,tech):
        self.technology=tech
    def get_technology(self):
        return self.technology
p1=programmer()
p1.set_name('john')
p1.set_salary(1000)
p1.set_technology(['java','python','c++'])
print(p1.get_name(),'\t',p1.get_salary(),'\t',p1.get_technology())        
        