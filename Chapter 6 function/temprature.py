def c_to_f(c):
    return (c * 9/5) + 32

c = int(input("Enter temperature in Celsius: "))
print(f"{c}°C is equal to {c_to_f(c)}°F")



#for converting fahrenheit to celcius

def f_to_c(f):
    return (f - 32) * 5/9

f = int(input("Enter temperature in Fahrenheit: "))
print(f"{f}°F is equal to {f_to_c(f)}°C")



#for both ==>


def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

choice = input("Enter 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").strip().upper()

if choice == 'C':
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c}°C is equal to {c_to_f(c)}°F")
elif choice == 'F':
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}°F is equal to {f_to_c(f)}°C")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")




