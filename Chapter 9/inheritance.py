class Employee:
    compnany = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary} ")

class Programmer(Employee):
    compnany = "ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and the salry is {self.salary} ")        


a = Employee() 
d = Programmer()

print(a.compnany, d.compnany)