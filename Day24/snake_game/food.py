from turtle import Turtle
import random


class Food(Turtle):#inheriting from turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self): #move to random location.
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        


#whenever you initialize a new object from a class the init gets called.