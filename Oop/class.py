'''
class Employee:
    language = "python"    # This is class attribute
    salary = 1200000

    # def __init__(self):        # Dunder method which is called automatically 
    #     print("I am creating an employee")

    def __init__(self,name,salary,lanuage):    # It will give the output for the given values
        self.name = name
        self.salary = salary
        self.language = lanuage
        print("I am creating an employee")

    def getinfo(self):
        print(f'The language is {self.language}. The salary is {self.salary}')

    @staticmethod     #It does not need an object so we use static metheod
    def greet():
        print('Good morning')



# this is for 2nd __init__ constructor
harry=Employee("Harry",130000,"C++")  
harry.greet()
harry.getinfo()


# this is for 1st __init__ constructor
# MK=Employee()
# MK.name="Momin"
# MK.language="JavaScript"   #  This is an instance attribute, it will over write class attribute
# print(MK.name,MK.language,MK.salary)

'''

'''
# Multiple inheritance

class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()
'''


'''
# Multilevel inheritance
class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)
'''


'''
# Use of super
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute 

# o = Programmer()
# print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)
'''


'''
# To over write class attribute over instance attribute by using @classmethod
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()
'''


'''
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Harry Khan"
print(e.fname, e.lname)

e.show()
'''

