marks = []

# Function to check if marks are passed or failed
def check_pass_fail(mark):
    if mark >= 50:
        return "Passed"
    else:
        return "Failed"

# Loop to input marks and check pass/fail status
for i in range(6):
    mark = int(input(f"Enter your marks for subject {i+1}: "))
    marks.append((mark, check_pass_fail(mark)))

# Print the marks along with pass/fail status
for index, (mark, status) in enumerate(marks):
    print(f"Subject {index + 1}: Marks = {mark}, Status = {status}")

