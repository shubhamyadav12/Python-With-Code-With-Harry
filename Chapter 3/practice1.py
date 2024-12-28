# # name = input("Enter your name: ")

# # print(f"good evening : {name}")


# letter = '''Dear Name,
# You are selected!
# date''' 

# print(letter.replace("Name", "shiva").replace("date", "30 May 2032"))




# Prompt the user for input
is_raining_input = input("Is it raining? (yes/no): ").strip().lower()
has_umbrella_input = input("Do you have an umbrella? (yes/no): ").strip().lower()
is_weekend_input = input("Is it the weekend? (yes/no): ").strip().lower()

# Convert the input to boolean values
is_raining = is_raining_input == "yes"
has_umbrella = has_umbrella_input == "yes"
is_weekend = is_weekend_input == "yes"

# Conditional statements based on the input
if is_raining and not has_umbrella:
    print("Stay inside.")
elif is_raining and has_umbrella:
    print("You can go outside with an umbrella.")
elif not is_raining and is_weekend:
    print("Perfect time for a hike!")
else:
    print("Enjoy your day.")