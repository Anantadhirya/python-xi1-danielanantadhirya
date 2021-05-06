class Person:
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

emp = Person("Joni")
print(emp.getName(), emp.isEmployee())

emp = Employee("Wawan")
print(emp.getName(), emp.isEmployee())