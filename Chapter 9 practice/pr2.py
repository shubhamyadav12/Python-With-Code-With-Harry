class Animal:
   pass

class Pet(Animal):
    pass

class Dog(Pet):

    @staticmethod 
    def bark(): 
        print("Bow Bow!")


o = Dog()         
o.bark()
# o = Pet()