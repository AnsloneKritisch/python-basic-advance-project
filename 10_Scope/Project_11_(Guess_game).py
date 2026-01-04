# It is a game of guessing a number between 1 and 100.
import random

# Generate a random number between 1 and 100
guess = random.randint(1, 100)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")


# Loop until the user guesses the correct number

while True:
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        attempts = 10
        print("You have 10 attempts to guess the number.")
        
    elif difficulty == 'hard':
        attempts = 5
        print("You have 5 attempts to guess the number.")
        
    else:
        print("Invalid input. Please type 'easy' or 'hard'.")

    while attempts > 0:

        user = int(input("Make a guess: "))

        attempts -= 1

        if attempts == 0:
            print(f"You've run out of guesses. The number was {guess}. You lose.")
            break
        if user == guess:
            print(f"You got it! The answer was {guess}.")
            break
        elif user < guess:
            print("Too low.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif user > guess:
            print("Too high.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print("Invalid input. Please enter a number between 1 and 100.")
            

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()

    if play_again == 'no':
        print("Thanks for playing! Goodbye.")
        break   
    elif play_again == 'yes':
        continue   
    else:
        print("Invalid input. Exiting the game.")
        break



        
        


