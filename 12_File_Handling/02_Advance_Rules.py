# Yes, you can write in w mode, but you cannot read from it.

# Why?

# w = write-only
# When you open a file like:

# open("example.txt", "w")


# ✔ The file is created (or cleared if it existed)
# ✔ You can write to it
# ❌ You cannot read from it



# If you want read + write
# Use:

# "r+" → read + write (file must already exist)
# "w+" → write + read (file clears first)

# Example:
with open("example.txt", "r+") as file:
    # Let's read the file first
    content = file.read()
    print(content)

    # Now let's write something
    file.write("I am Anslone Kritisch.")


