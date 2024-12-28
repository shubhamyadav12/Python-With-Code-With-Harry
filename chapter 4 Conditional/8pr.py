my_marks = int(input("Enter your marks here: "))

if my_marks > 100 or my_marks < 0:
    print("Please enter valid marks between 0 and 100.")
elif my_marks >= 90:
    print("Your grade is A+ and your marks are", my_marks)
elif my_marks >= 80:
    print("Your grade is A and your marks are", my_marks)
elif my_marks >= 70:
    print("Your grade is B and your marks are", my_marks)
elif my_marks >= 60:
    print("Your grade is C and your marks are", my_marks)
else:
    print("You have failed and your marks are", my_marks)
