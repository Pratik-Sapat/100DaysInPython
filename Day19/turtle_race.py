from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
#to set width and height of screen
screen.setup(width = 500, height = 400)#
#pop-up to ask user for input.
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color: ")#

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80] #change y-axix
all_turtles = [] #to store all created turtle.

for turtle_index in range(6):
    new_turtle = Turtle(shape = "turtle") #object = class
    new_turtle.color(colors[turtle_index]) #get different colors 
    new_turtle.penup() #not going to pendown bcz we are moving the turtle.
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) #go to start of the screen.(left side of screen)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True #if user bet is available then only race will start.

while is_race_on: #this way we prevent the start of race. by using if first.
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)







screen.exitonclick()