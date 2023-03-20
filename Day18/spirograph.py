import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color =  (r,g,b) #tuple
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
# print(tim.heading())
screen = t.Screen()
screen.exitonclick()


#we did 360/size_og_gap just to get complete circle and stop.
#tim.heading() _ size of gap is for drawing next circle from +size_of_gap position.we are setting new heading for cursor. 