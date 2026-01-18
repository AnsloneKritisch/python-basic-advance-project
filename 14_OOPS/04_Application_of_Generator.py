def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Using the generator to read a large file line by line
file_path = 'large_file.txt'
line = read_large_file(file_path)
for i in line:
    print(i.strip())  # Using strip() to remove extra newlines