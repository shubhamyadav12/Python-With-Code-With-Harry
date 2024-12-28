class Employee:
    salary = 200
    increament = 20
      
    @property 
    def salaryAfterIncreament(self):
        return (self.salary + self.salary * self.increament/100)
    
    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self, salary):
        self.increament = ((salary/self.salary) + 1)*100

e = Employee()
e.salaryAfterIncreament = 60
print(e.increament)
