import os
import random
from hangman_art import stages, logo
from hangman_words import word_list  #OR import hangman_words and use hangman_words.word_list every time to use.

chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

# from hangman_art import logo , stages you can also write this.used here!
print(logo)

# print(f"the solution is {chosen_word}.")  to check what is the actual solution is.

display = []
word_length = len(chosen_word)

for letter in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system("cls")

    if guess in display:
        print(f"you already guesses: {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position : {position} \n current letter: {letter} \n Guessed letter: {guess}")
        if letter == guess: 
            display[position] = letter
        
    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word. you lose a life.")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print(f"You lose! \nand the correct answer is {chosen_word}")
        
    print(display) #replace _ with word or _ again.

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    #used hangman_are import stages here
    print(stages[lives])

