print("Welcome to the Tip Calculator and Bill Splitter")
total_bill = float(input("What is the total bill : "))

tip = float(input("What percentage tip would you like to give : "))

tip_amount = total_bill * (tip / 100)
total_bill = total_bill + tip_amount

people = int(input("How many people to split the bill : "))

bill_per_person = total_bill / people

pay = round(bill_per_person , 2)

print(f"Each person should pay : {pay}")


