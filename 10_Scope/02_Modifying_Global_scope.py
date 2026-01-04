# How to modify a global variable inside a function


enemies = 2 

def increase_enemies():
    global enemies  # this tells python that we want to use the global variable 'enemies'
    enemies += 3
    print(f"Enemies inside function: {enemies}")


# Running the function
increase_enemies()
print(f"Enemies outside function: {enemies}")



# But do remember that using global variables only when necessary is a good practice
# Such as some constants like pi = 3.14, gravity = 10 etc.