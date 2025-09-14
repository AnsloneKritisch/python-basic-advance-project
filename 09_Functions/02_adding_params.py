# This function takes three parameters: name, location, and age
# and prints a profile summary
# remember the order of parameters matters
def profile(name, location, age):
    print("Name:", name)
    print("Location:", location)
    print("Age:", age)

# calling the function with order of parameters as defined
profile("John", "New York", 30)

# calling the function with keyword arguments, order doesn't matter
profile(name="Mike", location="Los Angeles", age=25)


# both of them works just fine just use the way you feel easy 
