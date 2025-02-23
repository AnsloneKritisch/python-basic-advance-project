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


# for example

name = input("What is your name ?")
length_of_name = len(name)

# print(" The length of your name is " + length_of_name) ->  this will probably give you error messages
# name is str 
# length_of_name is int 
#  the is no way to add int and str 
# so you will get an error message

print("The length of your name is " + str(length_of_name))

#that's  how we solve it 
# In Python, you can convert any data type to any other type using the built-in functions. This is known as type conversion.




