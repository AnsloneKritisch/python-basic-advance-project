# Project to create a password generator
import random

letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbol = ["!","@","#","$","%","&","*","-","_","=","+","/","?","~","|","<",">"]
number = ["1","2","3","4","5","6","7","8","9","0"]

print("Welcome to the Python Password Generator!")

letter_count = int(input("How many letters would you like in your password? "))
symbol_count = int(input("How many symbols would you like in your password? "))
number_count = int(input("How many numbers would you like in your password? "))


# easy part 

# password = ""

# for i in range(1,letter_count+1):
#     password += random.choice(letter)

# for i in range(1,symbol_count+1):
#     password += random.choice(symbol)

# for i in range(1,number_count+1):
#     password += random.choice(number)


# hard part 

password_list = []

for i in range(1,letter_count+1):
    password_list.append(random.choice(letter))

for i in range(1,symbol_count+1):
    password_list.append(random.choice(symbol))

for i in range(1,number_count+1):
    password_list.append(random.choice(number))

print(password_list)
random.shuffle(password_list)
print(password_list)

final_pass = "".join(password_list)
print("Your Password is " , final_pass)