# Let's Understand Scope in Python

# Lemme show you and example firt 


enemies = 2 

def increase_enemies():
    enemies = 5
    print(f"Enemies inside function: {enemies}")


# Running the function
increase_enemies()
print(f"Enemies outside function: {enemies}")

# You expect the value of enemies to be 5 not 2 after incease_enemies() function is called.
# You can see that the value of enemies inside the function is different from the value outside the function.


# Let's see another example
def drink_potion():
    # i created a variable potion_strength inside the function
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)  # this will give an error because potion_strength is not defined outside the function



# so bacically the enemeies variable in example one is in the global scope
# and the potion_strength variable in example two is in the local scope

# Global Scope - Variables that are defined outside of a function , and can be used anywhere in the code
# Local Scope - Variables that are defined inside a function , and can only be used inside that function