# let's create an empty dictionary

fruits = {}

# let's add some key:value pairs to the dictionary
fruits["apple"] = "a red fruit"
fruits["banana"] = "a yellow fruit"
fruits["cherry"] = "a red fruit"
print(fruits)

# let's create a loop which will print all the keys in the dictionary

for key in fruits:
    print(key)

# so we can see that the loop is printing all the keys in the dictionary
# if we want to print all the values in the dictionary we can use the values() method
for value in fruits.values():
    print(value)

# if we want to print all the key:value pairs in the dictionary 

for value in fruits:
    print(value, fruits[value])

