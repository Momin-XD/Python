''' 
class programmer:
    company = 'Microsoft'
    def __init__(self,name,salary,desig):
        self.name=name
        self.salary = salary
        self.desig = desig
        print("Employee registerd")

    def getinfo(self):
        print(f"Employee's Salary is {self.salary} and designation is {self.desig}")
        

MK=programmer('Momin',5400000,'Senior Developer')
MK.getinfo()
'''


'''
class calculator:

    def __init__(self,n):
        self.n = n 
        
    @staticmethod
    def greet():
        print("hello there!")

    def sqr(self):
        print(f"Square of {self.n} = {self.n *self.n}")

    def cube(self):
        print(f"Cube of {self.n} = {self.n *self.n*self.n}")

    def root(self):
        print(f"Square root of {self.n} = {self.n**0.5}")

n= calculator(9)
n.greet()
n.sqr()
n.cube()
n.root()
'''


