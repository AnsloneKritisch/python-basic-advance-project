'''
Why Use Exception Handling?

Program Doesn’t Crash
If something goes wrong, your program won’t stop suddenly.
It keeps running safely.

Handles Unexpected Errors
User may type wrong input, file may not exist, internet may fail.

Exception handling catches these mistakes.
Shows Friendly Messages
Instead of scary error messages, you can show:
“Sorry, something went wrong.”

Helps Debugging
You can find what went wrong and fix it later.

Saves Important Data
Prevents the program from shutting down before saving files or results.

Better User Experience
Users don’t get confused or frustrated by crashes.
Keeps Code Clean

All error-handling logic stays in one place (try-except block),
instead of random if-else everywhere.

'''

# Exception handling makes your program safe, stable, and user-friendly even when errors happen.

# There are different types of exceptions like ValueError, TypeError, FileNotFoundError, etc.

# Name error 
# ------------

# a =  b
# print(a)
# NameError: name 'b' is not defined 

# now to manage this error we use exception handling

try:
    a=b 
except :
    print("The Variable is not defined.")

# Now if we want to see the error and we can you the error name in except block
try:
    a=b
except NameError as ex:
    print(ex)

# Zero Division Error
# --------------------


# a = 5/0
# print(a)

try:
    a = 5/0
except ZeroDivisionError as ex:
    print(ex)
    print("You cannot divide a number by zero.")


# Now what we have 2 error at once ? then 

try:
    a = 5/2
    b = c
except ZeroDivisionError as ex:
    print(ex)
    print("You cannot divide a number by zero.")
# here there is no error in division but there is error in b = c
# and it is not always possible to know the error so we can use the general error exception
except Exception as ex:
    print(ex)
    print("Something went wrong.")

# Exception is parent class of all the exceptions. So it should be used at last in except block.
# Exception is the general exception and can be used to catch any error. 

# ValueError
try :
    a = int(input("Enter a number: "))
    result = 10/a
except ValueError as ex:
    print(ex)
    print("Please enter a valid number.")
except ZeroDivisionError as ex:
    print(ex)
    print("You cannot divide a number by zero.")
except Exception as ex:
    print(ex)
    print("Something went wrong.")
# else will only be executed if there is no error in try block
else:
    print("Result is:", result)

# finally will always be executed whether there is an error or not
finally:
    print("Execution completed.(Will always execute)")