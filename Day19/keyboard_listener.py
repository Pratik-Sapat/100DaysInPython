from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

#to bind key strokes.
def move_forward():
    tim.forward(10)

screen.listen() #to start listning of events.

#when space key is pressed then trigger the function move_forward. don't use () this bracket after function name bcz fun should trigger only after pressing the key.
screen.onkey(key="space", fun=move_forward)
screen.exitonclick() 