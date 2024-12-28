marks = []

# Function to check if marks are passed or failed
def check_pass_fail(mark):
    if mark >= 50:
        return "Passed"
    else:
        return "Failed (Improve)"

# Loop to input marks and check pass/fail status
for i in range(6):
    mark = int(input(f"Enter your marks for subject {i+1}: "))
    marks.append((mark, check_pass_fail(mark)))

# Print the marks along with pass/fail status
total_marks = 0
for index, (mark, status) in enumerate(marks):
    total_marks += mark
    print(f"Subject {index + 1}: Marks = {mark}, Status = {status}")

# Calculate total marks and percentage
percentage = (total_marks / (6 * 100)) * 100

# Print total marks and percentage
print(f"\nTotal Marks: {total_marks} out of 600")
print(f"Percentage: {percentage:.2f}%")
