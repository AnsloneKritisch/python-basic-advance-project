# Creating a BLackJack Game 
# Rules of the Game
# The game is played with an infinite deck of cards. 
# The deck is divided evenly between the player and the dealer. 
# The player starts with two cards, one of the dealer's cards is hidden until the end of the game. 
# The player can request additional cards to be dealt, until they decide to stop. 
# Face cards (Jack, Queen, King) count at 10. 
# Aces count either as 1 or 11, whichever is more advantageous to the player. 
# The game ends when a player or the dealer decides to stop. 
# The player who closes with the highest hand wins. 
# If the hands are the same, it's a tie. 
# The game can be played with as many players as you want, but it is recommended to play with two or three.
# 21 is a blackjack, which is an automatic win unless the dealer also has a blackjack.
# If the player goes over 21, they bust and lose the game.
# If the dealer goes over 21, they bust and the player wins.

import random

def choose_card():
    """Returns a random card from the deck."""
    cards = ["A" , 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]  # 10 is for J, Q, K and 11 is for Ace
    return random.choice(cards)

print("Welcome to Blackjack!")
print("All the best!")
while True:
    
    # Player's turn
    player_cards = []
    player_score = 0
    for _ in range(2):
        card = choose_card()
        player_cards.append(card)
        if card == "J" or card == "Q" or card == "K":
            player_score += 10
        elif card == "A":
            if player_score + 11 > 21:
                player_score += 1
            else:
                player_score += 11
        else:
            player_score += card
    print(f"Your cards: {player_cards}, current score: {player_score}")

    # Dealer's turn
    dealer_cards = []
    dealer_score = 0
    for _ in range(2):
        card = choose_card()
        dealer_cards.append(card)
        if card == "J" or card == "Q" or card == "K":
            dealer_score += 10
        elif card == "A":
            if dealer_score + 11 > 21:
                dealer_score += 1
            else:
                dealer_score += 11
        else:
            dealer_score += card
    print(f"Dealer's first card: {dealer_cards[0]}")

    # Player's turn
    while player_score < 21:
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
        if should_continue == 'y':
            new_card = choose_card()
            player_cards.append(new_card)
            if new_card == "J" or new_card == "Q" or new_card == "K":
                player_score += 10
            elif new_card == "A":
                if player_score + 11 > 21:
                    player_score += 1
                else:
                    player_score += 11
            else:
                player_score += card 
            print(f"Your cards: {player_cards}, current score: {player_score}")
        else:
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print("You are done drawing cards. Now it's dealer's turn.")
            break

    # Dealer's turn
    while dealer_score < 17:
        new_card = choose_card()
        dealer_cards.append(new_card)
        if new_card == "J" or new_card == "Q" or new_card == "K":
            dealer_score += 10
        elif new_card == "A":
            if dealer_score + 11 > 21:
                dealer_score += 1
            else:
                dealer_score += 11
        else:
            dealer_score += card
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    # Determine the winner
    if player_score > 21:
        print("You went over. You lose 😤")
    elif dealer_score > 21:
        print("Dealer went over. You win 😁")
    elif player_score > dealer_score:
        print("You win 😃")
    elif player_score < dealer_score:
        print("You lose 😤")
    else:
        print("It's a tie 🙃")


    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again != 'y':
        break
        

    
