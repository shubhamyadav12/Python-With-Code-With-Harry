num1 = float(input("Enter Your first Value here: "))
num2 = float(input("Enter Your second Value here: "))
num3 = float(input("Enter Your Third Value here: "))
num4 = float(input("Enter Your Fourth Value here: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    greatest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    greatest = num2
elif num3 >= num2 and num3 >= num1 and num3 >= num4:
    greatest = num3
else:
    greatest = num4

print(f"The greatest number is: {greatest}")