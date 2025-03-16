import random 

r = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

p = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

s = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
print("Welcome to Rock Paper and Sissor Game! ")
choose = int(input("What do you want to choose Rock = 0 , Paper = 1 , Sissor = 2  : "))
enemy = [ 0 , 1 , 2 ]

enemy_choice = random.choice(enemy)

if choose == 0 :
    print("\nYou chose Rock")
    print(r)
    
    if enemy_choice == 1 :
        print("Computer chose Paper")
        print(p)
        print("Computer wins!")

    elif enemy_choice == 2 :
        print("Computer chose Sissor")
        print(s)
        print("You win!")

    else :
        print("Computer chose Rock")
        print(r)
        print("It's a tie!")

elif choose == 1 :
    print("\nYou chose Paper")
    print(p)
    
    if enemy_choice == 0 :
        print("Computer chose Rock")
        print(r)
        print("You win!")

    elif enemy_choice == 2 :
        print("Computer chose Sissor")
        print(s)
        print("Computer wins!")

    else :
        print("Computer chose Paper")
        print(p)
        print("It's a tie!")

elif choose == 2 :
    print("\nYou chose Sissor")
    print(s)
    
    if enemy_choice == 0 :
        print("Computer chose Rock")
        print(r)
        print("Computer wins!")

    elif enemy_choice == 1 :
        print("Computer chose Paper")
        print(p)
        print("You win!")

    else :
        print("Computer chose Sissor")
        print(s)
        print("It's a tie!")


else :
    print("\nInvalid choice!")
    print("Please choose between 0, 1 or 2.")




