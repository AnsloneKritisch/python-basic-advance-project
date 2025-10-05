# There are 2 typrs of functions
# 1. Function without return type
# 2. Function with return type

# Function without return type
def add(x, y):
    print("The sum is:", x + y)

add(2, 3)



# function with return type

def add(x, y):
    return x + y    

result = add(2, 3)
print("The sum is:", result)

# well basically both are same but the difference is
# in function without return type we can't store the result in a variable
# but in function with return type we can store the result in a variable and use it later in the program
# so it is better to use function with return type


# we can also return multiple values from a function



def add_subtract(x, y):
    return x + y, x - y

sum_result, subtract_result = add_subtract(5, 3)
print("The sum is:", sum_result)
print("The subtract is:", subtract_result)