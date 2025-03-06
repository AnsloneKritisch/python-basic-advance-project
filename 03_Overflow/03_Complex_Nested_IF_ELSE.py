# basically in if else only 2 conditions are checked right ???
# but what if we need to check more than 2 conditions ???

# let's talk about a rollercoaster ride 
# you need to pass 2 arguments -> height and age 

height = int( input("Enter your Height : "))

if height >= 120:
    age = int( input("Enter your age : "))
    
    if 18 <= age <= 50:
        bill = 100
        print("You can ride the rollercoaster")
        print("Your Fair price will be 100 rupees")
    
    elif age >= 60:
        bill = 50
        print("You can ride the rollercoaster")
        print(" Please follow the instructions and you need a young partner with you ! ")
        print("Your Fair price will be 50 rupees")
        
    else:
        bill = 0
        print("You can not ride the rollercoaster")
        
    #here is a  little twist like your ex twisted your mind right ??
    photo = input("if you want photo press - Y : ")
    
    if photo == "Y":
        bill += 5
    
    print(f"Your Total bill is {bill}")
        
    
    #so now lemme explain you - so actually when you get if , elif and else any one condition will run 
    #and it will print the statement which is related to that particular condition
    # and it will not check the rest of the conditions
    
    # but if you use 2 if then both if will be trigger and we can get 2 outputs
    # that what makes it different form them 
    
     
        
 
else:
    print("You can not ride the rollercoaster")
    print("You are too short to ride this ride")
    





