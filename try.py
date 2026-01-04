buy = {
    "water" : {
        "price" : 20,
        "quantity" : 100
    },
    "milk" : {
        "price" : 30,
        "quantity" : 500
    },
    "coffee" : {
        "price" : 10,
        "quantity" : 500
    }
}

for item in buy:
        print(f"{item} will cost {buy[item]['price']} rupees for {buy[item]['quantity']} units.")