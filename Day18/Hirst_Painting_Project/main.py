# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r #to get specific value of color.
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

#now we commented colorgram related code as we got a list of colors(color_list) from the above code.

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup() #to hide black line.
tim.hideturtle() #to hide turtle
color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]

#just setting tim position to draw.
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
###
number_of_dots = 100

for dot_count in range(1 , number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90) #face up
        tim.forward(50)
        tim.setheading(180) #face left

        tim.forward(500) #to come again in start position.
        tim.setheading(0) #to face right

screen = t.Screen()
screen.exitonclick()


#'''
# 0 -> Face right
# 90 -> Face Up
# 180 -> Face Left
# 270 -> Face Down
# '''
