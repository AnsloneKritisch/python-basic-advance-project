print(" Welcome To ANSLONE Pizzas!") 
print(" Have a bit Enjoy the life :) ")

size = input(" What Size do you like to have ( S , M , L ) : ")

pepperoni = input(" Do you want to add pepperoni ( Y , N ) : ")

cheese = input(" Do you want to add cheese ( Y , N ) : ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1

print(f" Your final bill is : {bill}")

 