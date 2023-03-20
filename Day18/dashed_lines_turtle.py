from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup() #no drawing
    tim.forward(10) #go forward for 10 pieces when pen is up(drawing blank space)
    tim.pendown() #pen is on the paper


screen = Screen()
screen.exitonclick()