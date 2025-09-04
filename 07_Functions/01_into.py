# how to create a function !

# first we use def keyword to create a function the name of the function is my_function 
def my_function():
    # once you create a function you can write code inside it 
    # which will run once you will call the function
    print("Hello")
    print("Bye")
    
# how to call a function 
my_function()

# you can call the function as many times as you want
my_function()

# sometimes you want to pass some input to the function
def my_function_with_input(name):
    print(f"Hello {name}")
    print("Bye")    

my_function_with_input("John")
my_function_with_input("Mike")

# This is a game where you have to move a turtle to the finish line
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fselect_collection_en.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json
# use a function to move the turtle to the finish line

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()