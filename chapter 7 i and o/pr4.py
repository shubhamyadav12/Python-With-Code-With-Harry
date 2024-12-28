word_to_replace = "donkey"
replacement = "####"

# Open the file and read its content
with open("file.txt") as f:
    content = f.read()

# Check if the word "donkey" is in the file content
if word_to_replace in content:
    # Replace "donkey" with "####"
    modified_content = content.replace(word_to_replace, replacement)
    print(modified_content)
else:
    print(f"'{word_to_replace}' is not found in the text file")
