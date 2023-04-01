import turtle as t
import random

tim = t.Turtle()
#now select color totally in random manner.
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270] #direction by angle.
tim.pensize(10) #cheange pen size.
tim.speed("fastest") #change speed.

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions)) #to pick random directions.