# Read file line by line

with open("example.txt", "r") as file:
    for line in file:
        # print(line)
        print(line.strip()) # To remove extra newlines


# Append mode
with open("example.txt", "a") as file:
    file.write("\nI am learning Python file handling.")

# Write a line of lines you want to add
lines_to_add = ["\nThis is the first line.\n","This is the secondline.\n", "This is the third line." ]

with open("example.txt", "a") as file:
    file.writelines(lines_to_add)

