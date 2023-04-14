from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black") #background color.
screen.title("Snake Game") #set window title
screen.tracer(0) #to turn off screen(animation)

snake = Snake() #calling snake class
food = Food() #food class.
scoreboard = Scoreboard()

#controlls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#

game_is_on = True
while game_is_on: #automatically move snake forward.
    screen.update() #refresh the screen.
    time.sleep(0.1) #screen update every 0.1 sec. #delay for 0.1 sec and then refresh the screen.
    snake.move()
    #detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail.
    #if head collides with any segments in the tail.
        #trigger game_over 
    for segment in snake.segments[1:]: #used slicing to skip first head.
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


    
    




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