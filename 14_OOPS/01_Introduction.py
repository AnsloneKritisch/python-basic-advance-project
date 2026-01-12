# Class is the blue print of the object
# Object is the instance of the class

class Car:
    pass
audi = Car()  #Creating an object of class Car
bmw = Car()
audi.windows = 4 #Adding attribute to the object
bmw.windows = 2

# Accessing the attributes of the object
print(type(audi))
print(audi)
print(audi.windows)


# But this is not a good way to create attributes for the object

class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age 


# creating an object
dog1 = Dog("Buddy", 3)
print(dog1)
print(dog1.name)
print(dog1.age)



# Let create an instance method for the class
class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof! Woof!") 

        # Instance method
    def get_age(self):
        print(f"{self.name} is {self.age} years old")



# creating an object
dog1 = Dog("Buddy", 3)
dog1.bark()
dog1.get_age()
