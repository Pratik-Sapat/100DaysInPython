from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANSE = 10 
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90) #to face north.

    #player controll
    def go_up(self):
        self.forward(MOVE_DISTANSE)

    def go_down(self):
        self.back(MOVE_DISTANSE)

    def go_left(self):
        self.goto(self.xcor()-10,self.ycor())

    def go_right(self):
        self.goto(self.xcor()+10,self.ycor())

    #

    def go_to_start(self):
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
