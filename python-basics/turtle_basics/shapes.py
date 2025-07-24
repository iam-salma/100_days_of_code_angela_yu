import random
from turtle import *

tim = Turtle()
scr = Screen()

colormode(255)

tim.width(4)
tim.speed("fastest")

scr.title("SHAPES")
scr.bgcolor("black")

for i in range(3, 11):
    tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    for j in range(0, i):
        tim.forward(100)
        tim.left(360 / i)

scr.exitonclick()
