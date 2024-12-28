# username = "admin"
# password = "1234"

# input_username = input("Enter username: ")
# input_password = input("Enter password: ")

# if input_username == username and input_password == password:
#     print("Login successful.")
# else:
#     print("Invalid credentials.")


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 != 0]
print(even_numbers)

is_raining = True
has_umbrella = False
is_weekend = True

if is_raining and not has_umbrella:
    print("Stay inside.")
elif is_raining and has_umbrella:
    print("You can go outside with an umbrella.")
elif not is_raining and is_weekend:
    print("Perfect time for a hike!")
else:
    print("Enjoy your day.")

