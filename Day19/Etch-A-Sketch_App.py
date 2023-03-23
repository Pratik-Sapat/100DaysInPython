from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10 #degree
    tim.setheading(new_heading)
    #or 
    # tim.left(10) #10 degree

def turn_right():
    new_heading = tim.heading() - 10 #degree
    tim.setheading(new_heading)
    #or 
    # tim.right(10) #10 degree

def clear():
    tim.clear() #to clear the drawing
    tim.penup() #to prevent drwaing its path for riching home.
    tim.home() #moves the turtle to the origin which is in the middle of the screen
    tim.pendown() #ready for next drawing.

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()




