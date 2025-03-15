import random 

india = [ " Delhi " , " Mumbai " , " Chennai " , " Kolkata " , " Bangalore " ]

# first methord is using index number to get the random data

choose = random.randint(0,3)
print("You choose: ", india[choose])

# second methord is using random.choice() function to get random data

choose = random.choice(india)
print("You choose: ", choose)

