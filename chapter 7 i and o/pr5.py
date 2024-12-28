words_to_replace = ["donkey", "good", "about", "boy"]
# replacement = "####"

# Open the file and read its content
with open("file.txt") as f:
    content = f.read()

# Replace each word in the words_to_replace list with the replacement
for word in words_to_replace:
    if word in content:
        content = content.replace(word, "#"* len(word) )

# Print the modified content
print(content)
