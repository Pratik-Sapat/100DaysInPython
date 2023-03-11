# import turtle
# tim = turtle.Turtle()

from turtle import Turtle, Screen
tim = Turtle()
print(tim)

#change shape of cursor to turtle.
tim.shape("turtle")
#change color.
tim.color("coral")
#turtle move forward to 100
tim.forward(100)



my_screen = Screen()
print(my_screen.canvheight)
#allow to continue run screen until we click.
my_screen.exitonclick()
