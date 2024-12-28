def generatetTable(n):
    # Initialize an empty string to accumulate the multiplication table
    table = ""
    # Loop to generate multiplication results from 1 to 10
    for i in range(1, 11):
        # Format the current multiplication result and add it to the table string
        table += f"{n} x {i} = {n*i}\n"
    # Open a file in write mode to save the table
    with open(f"tables/table_{n}.txt", "w") as f:
        # Write the accumulated table string to the file
        f.write(table)

# Loop to generate tables for numbers from 2 to 20
for i in range(2, 21):
    # Call the function to generate and save the table for the current number
    generatetTable(i)
