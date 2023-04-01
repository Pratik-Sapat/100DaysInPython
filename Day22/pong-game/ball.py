from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 #reverse direction.

    def bounce_x(self):
        self.x_move *= -1 #reverse direction.
        self.move_speed *= 0.9 #each time increase in ball speed.

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1 #once player loss back to original speed.
        self.bounce_x() #after miss ball start going to opposite direction