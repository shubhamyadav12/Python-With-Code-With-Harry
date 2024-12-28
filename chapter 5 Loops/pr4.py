n = int(input("Cheak the number even or odd : "))

for i in range(1):
    if n % 2 != 0:
        print("this is odd number")
    else:
        print("this is even number")    


        #prime number cheak method

n = int(input("Cheak the number prime or not : "))

for i in range(2, n):
    if n%i == 0:
        print("number is not prime")
        break       
    else:
        print("number is prime")


