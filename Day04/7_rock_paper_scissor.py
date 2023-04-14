import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
#to get images in output we put it in list so its easy to get img according to choice.
game_images = [rock, paper, scissors]

#user chose
user_choice = int(input("What do you chose? type 0 for rock, 1 for paper or 2 for scissors.\n"))
print(game_images[user_choice])

#computer chose
computer_choice = random.randint(0, 2)
print("Computer Chose : ")
print(game_images[computer_choice])


#logic
if user_choice>= 3 or user_choice < 0:
    print("you typed invalid number you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!") 
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("it's draw")