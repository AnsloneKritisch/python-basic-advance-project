# Let's talk about iterables in Python
# An iterable is an object that can be iterated over (looped through)
# Examples of iterables: lists, tuples, strings, dictionaries, sets

# Let's create a list and iterate over it using a for loop first
my_list = [ 1 , 2 , 3 , 4]
for i in my_list:
    print(i)

# Let's talk about iterators in Python
# An iterator is an object that represents a stream of data.
# It implements two methods: __iter__() and __next__()
# The __iter__() method returns the iterator object itself.
# The __next__() method returns the next item in the sequence.
# When there are no more items, it raises the StopIteration exception.
# Lazy loading is a key feature of iterators, meaning they generate items on-the-fly and do not store them in memory.

# Let's talk how to create iterators in Python
iterator = iter(my_list)
print(type(iterator))
print(iterator)
print(next(iterator))
print(next(iterator))

# This example shows how to manually iterate using the iterator


# Using a try-except block to handle StopIteration
try:
    while True:
        item = next(iterator)
        print(item)
except StopIteration:
    print("No more items to iterate.")