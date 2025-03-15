#List ~ A list is a collection of items in a particular order.

# Now pls! don't forget list should be under " [] "  these brackets

# this is an integer list

numbers = [1, 2, 3, 4, 5]
print(numbers)

# this is a string list  
# Let's create a list of cities of India
india = [ " Delhi " , " Mumbai " , " Chennai " , " Kolkata " , " Bangalore " ]
print(india)

# hola hola ~ a biggest doubt you have in your is how will you access data right 
# for varibles which have only single data in it you can easily access it just by print(varible_name)
# but here you have muntiple data in your list so how will you access them ??

# HITS HARD ~ like your ex heart a lot of guy how will you take them out 

# We will use gun no I mean 

print(india[0])

india[4] = "Haryana "

print(india)

india.extend(["Banglore", "Patna", "Pune"])

print(india)



