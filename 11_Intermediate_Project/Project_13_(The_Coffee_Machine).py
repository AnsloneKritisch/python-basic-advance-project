# Coffee machine program

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# After Making the Menu and resources dictionarys .

# You need to understand 

# def check_resources(choice):
#     for item in MENU[choice]["ingredients"]:

print( MENU["espresso"]["ingredients"]["water"])
print( resources["water"])

for i in MENU["espresso"]["ingredients"]:
    print( i , MENU["espresso"]["ingredients"][i])
    print( i ,resources[i])
