marks = []

# Function to check if marks are passed or failed
def check_pass_fail(mark):
    if mark >= 50:
        return "Passed"
    else:
        return "Failed (Improve)"

# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'F'

# Loop to input marks and check pass/fail status
for i in range(6):
    mark = int(input(f"Enter your marks for subject {i+1}: "))
    marks.append((mark, check_pass_fail(mark)))

# Print the marks along with pass/fail status
total_marks = 0
highest_marks = -1
lowest_marks = 101
failed_subjects = []

for index, (mark, status) in enumerate(marks):
    total_marks += mark
    if mark > highest_marks:
        highest_marks = mark
    if mark < lowest_marks:
        lowest_marks = mark
    if "Failed" in status:
        failed_subjects.append(index + 1)
    print(f"Subject {index + 1}: Marks = {mark}, Status = {status}")

# Calculate total marks and percentage
percentage = (total_marks / (6 * 100)) * 100

# Calculate grade
grade = calculate_grade(percentage)

# Print total marks, percentage, and grade
print(f"\nTotal Marks: {total_marks} out of 600")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

# Print highest and lowest marks
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")

# Print subjects that need improvement
if failed_subjects:
    print("Subjects that need improvement: " + ", ".join(map(str, failed_subjects)))
else:
    print("All subjects passed!")
