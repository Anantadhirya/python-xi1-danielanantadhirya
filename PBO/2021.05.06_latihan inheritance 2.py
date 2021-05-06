class Person:
    def __init__(self, name, idn):
        self.__name = name
        self.__idn = idn
    def display(self):
        print(self.__name, self.__idn, sep='\n')

class Employee(Person):
    def __init__(self, name, idn, salary, post):
        Person.__init__(self, name, idn)
        self.__salary = salary
        self.__post = post

a = Employee("Rahul", 886012, 200000, "Intern")
a.display()