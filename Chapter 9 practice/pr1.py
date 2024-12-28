class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
        
    def show(self):
        super().show()
        print(f" + {self.k}k")

# Creating instances and calling show method
o = TwoDVector(1, 2)
o.show()  # Output: The vector is 1i + 2j

a = ThreeDVector(1, 2, 3)
a.show()  # Output: The vector is 1i + 2j + 3k
