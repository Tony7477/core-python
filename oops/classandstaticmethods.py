#class and static methods 
#classmethods can be used to alternative to constructors
import datetime
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
    
    #this equals to Employee.raise_amount=something this works even with emp1.raise_amount=something still 
    #everything would same . 
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def fromstring(cls,emp_str):
        firstname,pay=emp_str.split("-")
        return cls(firstname,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday==5 or day.weekday==6:
            return False 
        return True

#Employee.set_raise_amt(12)

emp1=Employee("tony",20)
emp1.set_raise_amt(12)
emp2=Employee.fromstring("hari-20")


print(emp1.raise_amount)
print(Employee.raise_amount)

mydate=datetime.date(2016,7,11)
print(Employee.is_workday(mydate))

