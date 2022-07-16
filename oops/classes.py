#useful for code reusability
class Employee:
    #class variables
    num_employees=0
    raise_amount=1.04


    def __init__(self,firstname,pay):
        #attributes or instance variables
        self.firstname=firstname
        self.pay=pay
        self.email=firstname+'.'+'@gmail.com'
        Employee.num_employees+=1


    
    #methods
    def taxDeduction(self):
        return self.pay*0.01
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
        

#instances
emp_1=Employee("hari",6789)
#method
#print(Employee.taxDeduction(emp_1))

print(emp_1.raise_amount)

Employee.raise_amount=1.05

emp_1.raise_amount=1.06
print(emp_1.__dict__)
print(Employee.__dict__)
emp_1.apply_raise()
print(emp_1.pay)

#print(emp_1.pay)
#print(emp_1.taxDeduction())
emp_2=Employee("bis",8099)
print(Employee.num_employees)





        
    



"""emp_1=Employee()
#attiributes
emp_1.firstname="haro"
emp_1.lastname="kom"
emp_1.pay=700
print(emp_1.pay)
emp_2=Employee()"""

#class variables
    


    














