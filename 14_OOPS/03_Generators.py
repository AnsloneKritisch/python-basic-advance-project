def square(n):
    for i in range(n):
        return i ** 2

sq = square(3)
print(sq)

# Output: 0 
# The function returns immediately after the first iteration
# So the output is 0

# Question is how to make it return all the squares one by one?
# The answer is to use 'yield' keyword instead of 'return' keyword

# Let's modify the function to use 'yield'
def square_generator(n):
    for i in range(n):
        yield i ** 2

sq = square_generator(3)
print(sq)

# Output: <generator object square_generator at 0x7f9b8c0d4c10>
# The function now returns a generator object instead of a single value
# What does this means?
# A generator is a special type of iterator that generates values one by one 
# It just means a generator is created which can be used to get the squares one by one

# METHORD  1: Using a for loop to get all the values from the generator

# for i in sq:
#     print(i)

# actually we needed a loop to simply get all the values 
#  BUT IS THERE ANY OTHER WAY TO GET THE VALUES ONE BY ONE?
# Yes, we can use the 'next()' function to get the next value from the generator

# METHORD 2: Using next() function to get the values one by one
print(next(sq))
print(next(sq))
print(next(sq))

# ------------------------------------------------------------------------------------------

# WHAT ELSE ?
# Can we have multiple 'yield' statements in a single function?
def multi_yield():
    yield "First yield"
    yield "Second yield"
    yield "Third yield"

gen = multi_yield()
print(next(gen))  # Output: First yield
print(next(gen))  # Output: Second yield    
print(next(gen))  # Output: Third yield

# you can use the loop too
for i in gen:
    print(i)  # No output as all values are already consumed