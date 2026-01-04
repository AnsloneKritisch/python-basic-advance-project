# Coffee machine program

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

buy = {
    "water" : {
        "price" : 20,
        "quantity" : 100,
        "unit" : "ml"
    },
    "milk" : {
        "price" : 30,
        "quantity" : 500,
        "unit" : "ml"
    },
    "coffee" : {
        "price" : 10,
        "quantity" : 500,
        "unit" : "gm"
    }
}


# After Making the Menu and resources dictionarys .

# ------ TODO 1: Learn How to access the values of the dictionary ------

# You need to understand how to access the values of the dictionarys.

# To access the values of MENU
# print( MENU["espresso"]["ingredients"]["water"])

# To access the values of Resouces
# print( resources["water"])

# To access the values of MENU and resources at the same time using loop
# for i in MENU["espresso"]["ingredients"]:
#     print( i , MENU["espresso"]["ingredients"][i])
#     print( i ,resources[i])

# To access the values of MENU
# for item in MENU:
#     print(item, MENU[item])
#     for ingredient in MENU[item]["ingredients"]:
#         print(f"  {ingredient}: {MENU[item]['ingredients'][ingredient]}")

# ------ TODO 2: Create a function to check resources availability ------
def check_resources(choice):
    for item in MENU[choice]["ingredients"]:
        if resources[item] < MENU[choice]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# ------ TODO 3: Create a function to process coins ------
def process_coins(choice):
    print(f"Please insert {MENU[choice]['cost']} rupees for {choice}.")
    money = int(input("Please insert money here (in rupees): "))

    if money < MENU[choice]['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif money == MENU[choice]['cost']:
        return True
    elif money > MENU[choice]['cost']:
        change = money - MENU[choice]['cost']
        print(f"Here is {change} rupees in change.")
    return True

# ------ TODO 4: Create report function ------
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print("Items is available for purchase")
    c , l , e = 0 , 0 , 0
    for items in MENU:
        for res in MENU[items]["ingredients"]:
            if resources[res] > MENU[items]["ingredients"][res]:
                if items == "cappuccino":
                    c =+ 1
                elif items == "latte":
                    l =+ 1
                elif items == "espresso":
                    e =+ 1
    print(f"Espresso: {e}cup \nLatte: {l}cup \nCappuccino: {c}cup")

# ------ TODO 5: Create main function ------

def buy_resource():
    print("What would you like to buy?")
    for item in buy:
        print(f"{item} will cost {buy[item]['price']} rupees for {buy[item]['quantity']} {buy[item]['unit']}.")
    choice = input("Enter your choice: ").lower()
    unit = int(input(f"How many units of {choice} would you like to buy? "))
    if choice in buy:
        cost = buy[choice]['price'] * unit
        total_quantity = buy[choice]['quantity'] * unit
        print(f"You have selected {choice} \n It will cost {cost} rupees \n {total_quantity} {buy[choice]['unit']} {choice} will be added to your cart.")
        money = int(input("Please insert money here (in rupees): "))
        if money >= cost:
            resources[choice] += total_quantity
            change = money - cost
            print(f"Here is {change} rupees in change.")
            print(f"Here is your {choice}. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Invalid choice. Please choose again.")



# ------ TODO 6: Create main function ------

def coffee_machine():
    print("Welcome to the Coffee Machine!")
    print("Type 'off' to turn off the machine.")
    print("Type 'report' to view the resource report.")
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Turning off the machine. Thank you! ")
            is_on = False
        elif choice == "report":
            report()
        elif choice in MENU:
            if check_resources(choice):
                if process_coins(choice):
                    for item in MENU[choice]["ingredients"]:
                        resources[item] -= MENU[choice]["ingredients"][item]
                    print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry, there are not enough resources to make that drink.")
                ask_buy = input("Would you like to buy resources? (yes/no): ").lower()
                if ask_buy == "yes":
                    buy_resource()
                else:
                    print("Goodbye!")
        else:
            print("Invalid choice. Please choose again.")


# # ------ TODO 7: Run the coffee machine ------
coffee_machine()