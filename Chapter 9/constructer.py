class Employee:
    def __init__(self):
        print("constructer of employee")
    a = 1

class Programmer(Employee):
      def __init__(self):
        super().__init__()
        print("constructer of Pragrammer")
      b = 2


class Manager(Programmer):
      def __init__(self):
        super().__init__()
        print("constructer of Manager")
      c = 3


# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)