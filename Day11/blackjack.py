import os
import random
from art import logo
#Hint 4 : 
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Hint 6
def calculate_score(cards):
    """take a list of cards and returned score calculated from the cards"""
    #cards = [1,2,3,4] = summ=10
    #Hint 7:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Hint 8:
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Hint 13:
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21: #if both get over you lose.
        return "You went over. You lose"

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You Lose."
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You lose"

def play_game():
    print(logo)
    #Hint 5:
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2): #_ because we don't need any variable.
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Hint 11:
    while not is_game_over:
        #Hint 9:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score : {user_score}")
        print(f"computer first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #Hint 10:
            user_shoulld_deal = input("type 'y' to get another card, type 'n' to pass: ")
            if user_shoulld_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Hint 12:
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand is : {user_cards}, final score : {user_score}")
    print(f"computer's final hand is : {computer_cards}, final score : {computer_score}")
    print(compare(user_score, computer_score))

#Hint 14:
while input("Do you want to play a game of Blackjacl? Type 'y' or 'n' : ") == 'y':
    os.system("cls")
    play_game()

