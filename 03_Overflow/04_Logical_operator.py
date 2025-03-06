# come let talk about operators 
#  first comes -> and operator -> && operator -> only if both conditions are true then it will be true
#  second comes -> or operator -> || operator -> if any one condition is true then it will be true
#  third comes -> not operator -> ! operator  -> it converts any date , true becomes false and false becomes true

a = 12 
print(a > 10 or a < 10)

b = 15
print(b > 10 and b < 10)



age = int(input("Enter you age :"))

if( age >= 40  and age <= 59 ):
    print("You are a middle age man")
else :
    print( "You are good to go !")
    