# dictonary is a collection which is unordered, changeable and indexed. In Python dictonary is written in curly brackets {} and key:value pair is separated by comma.

# example

fruits = {
    "apple": "a red fruit",
    "banana": "a yellow fruit",
    "cherry": "a red fruit"
}

print(fruits)

# here apple is key and a red fruit is value. we can access the value by using key.

# accessing value by key
print(fruits["apple"])

# we can also use get() method to access the value by key
print(fruits.get("banana"))

# we can change the value of a key
fruits["cherry"] = "a dark red fruit"
print(fruits)

# we can add new key:value pair to the dictonary

fruits["orange"] = "a orange fruit"
print(fruits)

# we can remove a key:value pair from the dictonary using pop() method
fruits.pop("banana")
print(fruits)

# we can also use del keyword to remove a key:value pair
del fruits["apple"]
print(fruits)

