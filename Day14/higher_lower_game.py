from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    "takes account data and returns the printable format."
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """take user guess and follower count and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #generate random account from game data.
    #making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    #format account data 
    print(f"Compare A : {format_data(account_a)}.")
    print(vs)
    print(f"Compare B : {format_data(account_b)}.")

    #ask user for guess.
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
    #get follower count.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #clear() screen
    os.system("cls")
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score : {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
