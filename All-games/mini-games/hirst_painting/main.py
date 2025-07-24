import random
from turtle import *

tim = Turtle()
scr = Screen()

colormode(255)

tim.speed("fastest")

scr.title("HIRST PAINTING")
scr.bgcolor("black")

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
                (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
                (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
                (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
                (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.setheading(315)
tim.up()
tim.forward(400)
tim.setheading(0)

for _ in range(10):
    tim.up()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)
    tim.down()

    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.up()
        tim.forward(50)
        tim.down()


scr.exitonclick()
