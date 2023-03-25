from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black") #background color.
screen.title("Snake Game") #set window title
screen.tracer(0) #to turn off screen(animation)

game_is_on = True
snake = Snake() #calling snake class

#controlls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#

while game_is_on: #automatically move snake forward.
    screen.update() #refresh the screen.
    time.sleep(0.1) #screen update every 0.1 sec. #delay for 0.1 sec and then refresh the screen.

    snake.move()


screen.exitonclick()







#comments : 
#one way to crate turtle one after another we did using for loop in code.
    # segment_1 = Turtle("square") #square turtle
    # segment_1.color("white")
    # segment_2 = Turtle("square")
    # segment_2.color("white")
    # segment_2.goto(-20,0)
    # segment_3 = Turtle("square")
    # segment_3.color("white")
    # segment_3.goto(-40,0)

#for smooth animation.
    #screen.tracer(0)=> #to turn off screen(animation)
    #screen.update() =>#update screen each time.for smooth view.a counter to tracer function to start screen again.