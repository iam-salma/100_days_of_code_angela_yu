import random
from turtle import *

tim = Turtle()
scr = Screen()

colormode(255)

tim.width(8)
tim.speed("fastest")

scr.title("RANDOM WALK")
scr.bgcolor("black")

direction = [90, 180, 270, 360]

for i in range(0, 50):
    tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    tim.forward(25)
    tim.setheading(random.choice(direction))

scr.exitonclick()
