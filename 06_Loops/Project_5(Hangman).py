# This is the hangman game
import random

"""
# First I tool a list of words
list_of_words = ["ardvark", "baboon", "camel"]

# imported random module to choose a random word from the list
import random

# choose a random word from the list
chosen_word = random.choice(list_of_words)

# find the length of the chosen word
word_length = len(chosen_word)  

print(f"The chosen word is {chosen_word}")
print(f"The length of the chosen word is {word_length}")

# create a variable to store the number of chances the user has
num = word_length

# displayinq the blank spaces for the chosen word
display = ["_"] * word_length  
print(display)

# creating a loop where we will ask the user to guess a letter the number of times will be equal to the length of the chosen word

while num > 0:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:

        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
                print(display)
        print("You successfully guessed a letter!")

    else:
        print("You guessed a wrong letter!")
        print("You got" , num ,"chances left")

    num -= 1

    """

###########################################################

word_list = ["ardvark", "baboon", "camel"]

# todo 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it to the console to check that you've chosen the word correctly. Hint: Remember to import the random module first. 🎲

chosen_word = random.choice(word_list)
# print(chosen_word , "is the chosen word")

#todo 4 - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"]. Hint: Remember that a List is a collection of items.

word_length = len(chosen_word)

display = ["_"] * word_length 

print(display)

# todo 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Guess a letter: ").lower()

# todo 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. If it is, print "Right" on the console, otherwise print "Wrong".

# for letter in chosen_word:
    # print(letter)
    # if letter == guess:
    #     print("Right")
    # else:
    #     print("Wrong")


# todo 5 - Loop through each position in the chosen_word; if the letter at that position matches 'guess' then reveal that letter in the display at that position. For example, if the user guessed "p" and the chosen_word was "apple", then display should be ["_", "p", "p", "_", "_"]. Hint: You'll need to loop through the string and find the index of each letter, so using a for loop combined with range() will be helpful. e.g. for position in range(word_length).

# for i in range(word_length):
#     letter = chosen_word[i]
#     if letter == guess:
#         display[i] = letter

# print(display)



# todo 6 - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more "_" characters. Then you can tell the user they've won.

# while "_" in display:
#     guess = input("Guess a letter: ").lower()

#     for i in range(word_length):
#         letter = chosen_word[i]
#         if letter == guess:
#             display[i] = letter

#     print(display)

# todo 7 - create a variable called 'lives' to keep track of the number of lives the user has. Set 'lives' to equal 6.

lifes = 6

# todo 8 - create stages of hangman as a list of strings.
stages = ['''
  +---+
  |   |
  O   |
 /|\  | 
 / \  |         
''', '''
  +---+
  |   |
  O   |
 /|\  | 
 /    |         
''', '''
  +---+
  |   |
  O   |
 /|\  | 
      |         
''', '''
  +---+
  |   |
  O   |
 /|   | 
      |         
''', '''
  +---+
  |   |
  O   |
  |   | 
      |         
''', '''    
  +---+
  |   |
  O   |
      | 
      |         
''', '''
  +---+
  |   |
      |
      | 
      |         
''']

# todo 9 - if the letter is not in the chosen_word, then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You lose."

# while lifes > 0:
    
#     guess = input("Guess a letter: ").lower()

#     if guess in chosen_word:

#         for i in range(word_length):
#             letter = chosen_word[i]
#             if letter == guess:
#                 display[i] = letter

#         print(display)

#         if "_" not in display:
#             print("You win!")
#             break

#     else:
#         lifes -= 1
#         print(f"You guessed a wrong letter. You have {lifes} lives left.")
#         if lifes == 0:
#             print("You lose.")
#             print(f"The word was {chosen_word}")

#     print(stages[lifes])



# toda 10 - Improving the game experience

while lifes > 0:
    
    guess = input("Guess a letter: ").lower()

    print("xxxxxx You have " , lifes , "lives left xxxxxx")

    if guess in chosen_word:

        for i in range(word_length):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = letter

        print(display)

        if "_" not in display:
            print(" ------ You win! -----")
            print("------ Congratulations Yay !!  -----")
            break

    else:
        lifes -= 1
        print(f"xxxxxxxxxx You guessed a wrong letter. xxxxxxxx")
        print(f"xxxxxxxxxx You have {lifes} lives left. xxxxxxxxxxxx")
        if lifes == 0:
            print("You lose.")
            print(f"The word was {chosen_word}")

    print(stages[lifes])

