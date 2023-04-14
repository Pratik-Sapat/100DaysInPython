print("Welcome to Tresure Island.")
print("Your mission is to find the tresure.")
 
choice1 = input('you\'re at a crossroad , where do you want to go ? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to the lake . there is an island in the middle of the lake. type "wait" to wait for a boat. type "swim" to swim across.').lower()

    if choice2 == "wait":
        choice3 = input("you arrive at the island unharmed. There is house with 3 doors. one red, onre yellow and one blue. which colour do you choose? ").lower()

        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! you Win!")
        elif choice3 == "blue":
            print("you enter a room of beasts. Game over.")
        else:
            print("you chose a door that doesn't exist. Game over.")          
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

