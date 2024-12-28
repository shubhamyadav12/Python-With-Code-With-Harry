class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n     
           
a = Number(1)
b = Number(2)

print(a + b)