def divisible5(n):
    if(n%5 == 0): 
     return True
    return False 

a = [1, 2, 3453, 432, 3242]

f = list(filter(divisible5, a))
print(f)