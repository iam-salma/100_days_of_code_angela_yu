from turtle import *

tim = Turtle()
scr = Screen()

tim.color("gold")

scr.title("A DASHED LINE")
scr.bgcolor("teal")

for i in range(0, 20):
    tim.down()
    tim.forward(10)
    tim.up()
    tim.forward(10)

scr.exitonclick()
