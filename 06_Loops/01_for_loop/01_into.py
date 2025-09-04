# loops are basically means to cycle through a process as many times as you want 
# for loop is a type of loop where you take variables and store your loop data in it 

#if you want to print 1 - 10 using loop then
# in range we write (start, end, step) ,  but the end is included with one less so add +1 to get you required output
# for 1 - 10 our end will be 11  

for i in range(1, 11):
    print(i)

# if you want to print 10 - 1 using loop then 

for i in range(10, 0, -1):
    print(i)

# loop in a list is used like this
fruits = ["apple", "orange", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    

    