#there are lot of data types available one of them is String

print (" Hello ") #this is a string

# the surpise is that we can slice sting data and very easily
# just like she sliced your heart in 2 , hahaha 

print ("Hello " [0]) # prints first character of the string
print ("Hello " [1]) # prints second character of the string
print ("Hello " [2]) # prints third character of the string

print ("Hello " [0:3]) # prints characters from 0 to 2 (not including 3)

#now the question why 0 ? why not 1 ? for printing the first character
# The answer is index number , what is it ???? 
# sting    =  H E L L O
# index no =  0 1 2 3 4
# so the first character is at index 0 , second is at index 1 and so on...

# we can also use negative index to print characters from end of the string
print ("Hello " [-1])
print ("Hello " [-2])
print ("Hello " [-3])

print ("Hello " [-4:]) # prints characters from -4 to end of the string

# and of course we can slice string with step parameter
print ("Hello " [0:4:2])

# this will print characters from 0 to 3 (not including 4) with step 2

print ("Hello " [::-1]) # prints string in reverse order

