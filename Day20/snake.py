from turtle import Turtle

#constant.
SARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        #this line always write after snake created. 
        self.head = self.segments[0] 

    def create_snake(self):
        for position in SARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        #to follow segment path next to every segment.
        for seg_num in range(len(self.segments)-1, 0, -1):#(strt, stop, step)
            new_x = self.segments[seg_num - 1].xcor()#x position of next(second-last) segment 
            new_y = self.segments[seg_num - 1].ycor() #y position of next(second-last) segment.
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE) #move first segment forward

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


#comments:

# heading() ->turtle method which gives the direction in turms of this 360 degreee number and (used to check if equal to other degree in program.)