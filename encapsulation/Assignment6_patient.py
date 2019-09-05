class patient:
    def set_id(self,id):  # @ReservedAssignment
        self.id=id
    def get_id(self):
        return self.id
    def set_name(self,name):  
        self.name=name
    def get_name(self):
        return self.name
    def set_ssn(self,ssn): 
        self.ssn=ssn
    def get_ssn(self):
        return self.ssn
p=patient()
p.set_id(123)
p.set_name('Bahare')
p.set_ssn(456)
print("Patient's Information\nName:",p.get_name(),"\nID:",p.get_id(),"\nSSN:",p.get_ssn())
    
        
        