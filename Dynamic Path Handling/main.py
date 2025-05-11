# os.getcwd() – current working directory

# os.path.join() – path creation

# os.path.abspath() – full absolute path

# os.path.exists() – check if path exists


import os

# Get current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# Join paths dynamically
folder = "test_folder"
file = "sample.txt"
file_path = os.path.join(current_dir, folder, file)
print("Dynamic File Path:", file_path)

# Convert relative to absolute path
abs_path = os.path.abspath(file_path)
print("Absolute Path:", abs_path)

# Check if file or folder exists
if os.path.exists(file_path):
    print("File exists at:", file_path)
else:
    print("File does not exist at:", file_path)
