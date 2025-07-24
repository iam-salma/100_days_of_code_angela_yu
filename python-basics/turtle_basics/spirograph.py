import random
from turtle import *

tim = Turtle()
scr = Screen()

colormode(255)
tim.speed("fastest")

scr.title("SPIROGRAPH")
scr.bgcolor("black")

for _ in range(36):
    tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    tim.circle(100)
    tim.left(10)

scr.exitonclick()
