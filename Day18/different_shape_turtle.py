from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ["red", "yellow", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SeaGreen"]
def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()