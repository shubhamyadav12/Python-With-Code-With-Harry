today = "sunday"
holiday = input("what id day today ?  ").strip().lower()

print("User entered:", holiday)  # This will show the cleaned and lowercased input


if holiday==today:
    print("yes we can enjoy today")
else:
    print("no we can not go anywhere")