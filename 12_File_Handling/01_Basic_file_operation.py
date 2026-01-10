# The most important step file operations in Python is to open a file using the built-in open() function.

file = open("example.txt", "r")

# After opening the file, you can perform various operations such as reading, writing, or appending data.

# Now you can read the contents of the file using the read() method.
content = file.read()
print(content)

# Writing to a file is another crucial operation. To write data, you need to open the file in write ('w')

file = open("example.txt", "w")
file.write("I am fine .")

# Well if you see your file now the previous content is erased and new content is written. " w" mode overwrites the existing content.


# Finally, it's important to close the file after completing the operations to free up system resources.
file.close()


'''-------------------------'''

# Well you know opening and closing files is kind a drag and take more lines time and effort.
# So Python provides a better way of handling files using the with statement.
#  Lemme explain you how it works.

with open("example.txt", "r") as file:
    content =  file.read()
    print(content)

with open("example.txt", "w") as file:
    file.write("I am good.")