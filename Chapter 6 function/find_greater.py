def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Inputs ko alag-alag variables me store karte hain
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
n3 = int(input("Enter your third number: "))

# Sabse bade number ko calculate karte hain
greatest_number = greatest(n1, n2, n3)

# Result ko print karte hain
print(f"The greatest number among {n1}, {n2}, and {n3} is : {greatest_number}.")



