# Function Copy

def welcome():
    return "Welcome to Python Decorators!"

wel = welcome()
print(wel)

# Well copy of function 

wel = welcome
wel() # Welcome function has been copied to wel without parentheses
print(wel())

# Now I am going to delete the welcome function
del welcome
# Now Let's see what happens when we call the welcome function
# print(welcome()) # NameError: name 'welcome' is not defined
# But we copyed the function to wel variable
print(wel()) # This will work fine


# Let's Create a sub-function
def main_welcome():
    def sub_welcome():
        return "Welcome to Python Decorators!"
    return sub_welcome

wel = main_welcome()
print(wel)