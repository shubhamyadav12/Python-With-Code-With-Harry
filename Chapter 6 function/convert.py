def i_to_c(inches):
    return inches*2.54
n = float(input("Enter here the number in inches  : "))
centimeters = i_to_c(n)
print(f"{n} inches is equal to {centimeters} centimeters.")
