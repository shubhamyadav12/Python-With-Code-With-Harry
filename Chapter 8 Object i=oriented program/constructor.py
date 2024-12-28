class Employee:
    language = "python"
    salary = 3000000

    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary} and the employee name is {shiva.name}")

    def __init__(self) -> None:
        print("i am creating an object")
        

    @staticmethod
    def greet():
        print(f"Good Day {shiva.name}")

shiva = Employee()    
shiva.name = "shiva"
# shiva.language = "JavaScript"
shiva.greet()
shiva.getinfo()