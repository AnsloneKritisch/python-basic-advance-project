# Creating a calculator using functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

result = 0

ask = input("Do you want to perform a calculation? (yes/no): ").lower() 

while ask == "yes":

    n1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    n2 = float(input("Enter second number: "))
    
    if operator == "+" :
        result = add(n1, n2)           
        print("The result is:", result)
    elif operator == "-" :
        result = subtract(n1, n2)
        print("The result is:", result)
    elif operator == "*" :
        result = multiply(n1, n2)
        print("The result is:", result)
    elif operator == "/" :
        result = divide(n1, n2)
        print("The result is:", result)
    else:
        print("Invalid operator!")

    continue_calculation = input("Do you want to continue calculation? (yes/no): ").lower()

    while continue_calculation == "yes":
        n3 = float(input("Enter next number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+" :
            result = add(result, n3)           
            print("The result is:", result)
        elif operator == "-" :
            result = subtract(result, n3)
            print("The result is:", result)
        elif operator == "*" :
            result = multiply(result, n3)
            print("The result is:", result)
        elif operator == "/" :
            result = divide(result, n3)
            print("The result is:", result)
        else:
            print("Invalid operator!")

        continue_calculation = input("Do you want to continue calculation? (yes/no): ").lower()
        
    
    ask = input("Do you want to perform another calculation? (yes/no): ").lower()





        
        
    