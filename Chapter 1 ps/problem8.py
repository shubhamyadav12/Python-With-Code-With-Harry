import os

def print_directory_contents(path):
    # List all files and directories in the given path
    contents = os.listdir(path)
    for item in contents:
        print(item)

# Example usage:
directory_path = '/users'
print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)
