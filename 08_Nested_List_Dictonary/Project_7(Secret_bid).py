# secret biding program

bid = {}

# name = input("Enter your name: ")
# bid_amt = int(input("Enter your bid amount: $"))
# bid[name] = bid_amt 
# print(bid)

while True :
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
    if continue_bid == "yes":
        name = input("Enter your name: ")
        bid_amt = int(input("Enter your bid amount: $"))
        bid[name] = bid_amt 

    elif continue_bid == "no":
        for key in bid:
            if bid[key] == max(bid.values()):
                # print(max(bid.values()))
                print(f"The winner is {key} with a bid of ${bid[key]}")
        break