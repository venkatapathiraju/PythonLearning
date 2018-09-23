class Person:
    'Comments on this class'
    def __init__(self, fname, lname):
        'Initialises two attributes of a person'
        self.fname = fname
        self.lname = lname



class Employee(Person):
    'Inheritance'
    all_employees = []
    def __init__(self, fname, lname, empid) :
        Person.__init__(self, fname, lname)
        self.__empid = empid
        Employee.all_employees.append(self)
        
    def getSalary(self):
        return 'You get Monthly salary'
        
    def getBonus(self):
        return 'You are eligible for Bonus'

    def get_empid(self):
        return self.__empid

class ContractEmployee(Employee):
    'Polymorphism'

    def getSalary(self):
        return 'You get Hourly salary'
    def getBonus(self):
        return 'You Won''t get bonus'



e = Employee('Howard', 'Chin', 1234)
print(e.get_empid())

c = ContractEmployee('Venkat','Raju',123)
print (c.getSalary())
