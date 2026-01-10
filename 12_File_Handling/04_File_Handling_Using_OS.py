import os

file_path = "example.txt"
if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")


file_size = os.path.getsize(file_path)
print(f"File size: {file_size} bytes")

old_file_path = "example.txt"
new_file_path = "new_example.txt"
os.rename(old_file_path, new_file_path)

file_path = "new_example.txt"
os.remove(file_path)