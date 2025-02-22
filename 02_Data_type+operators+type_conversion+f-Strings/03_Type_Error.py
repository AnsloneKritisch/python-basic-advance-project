# Working with type errors

# len(123)
# TypeError: object of type 'int' has no len()
# but 
len("Hello")
#you can see no error 

# So you should know each function works with as specified data type or arguments

# Now let's see how we can see any data type of any raw data 

print(type(123))

print(type("Hello"))

print(type(True))

print(type(12.5))

# what if you want to convert a data-type of any data 
print("12"+ " 13") 
# this is how you can convert a data-type of any data to get the required data-type
print(int("12") + int("13"))





