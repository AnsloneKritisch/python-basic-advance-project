#Let's Plan A GAME
print("\nThe Tresure Island")
print("Your mission is to find the Tresure")

print("\n Stage 1 \n")
print("You are in a dark, narrow cave with only two doors.")
print("Do you go through door #1 or door #2 ?\n")

door = input("Choose a door (1/2): ")
if door == "1":
    print("\nCongratulations you Choose the correct door \n")

    print("\n Stage 2 ")
    print("Now there is a River")
    print("Do you want to swim across the river or use the boat to cross it ? \n")

    river_choice = input("Choose (S)wim or (B)oat: ")
    if river_choice == "B":
        print("\nCongratulations you cross the river")

        print("\n Stage 3 \n")
        print("There are 3 doors in front of you")
        print("Red door , Blue door and Yellow door \n")

        door_choice = input("Choose a door (R/B/Y): ")
        if door_choice == "B":
            print("\nCongratulations")
            print("\nYou found the treasure")
            print("\nYOU WON \n")

        else:
            print("Choose the wrong door")
            print("\n Game Over \n")
            print("People Luckily put there hands on treasure ")

    else:
        print("The river had crocodile")
        print("\n Game Over \n")
        print("People Luckily put there hands on treasure ")
        
        
else:
    print("Sorry, you chose the wrong door")
    print("\n Game Over \n")
    print("People Luckily put there hands on treasure ")
    
