from turtle import *

tim = Turtle()
scr = Screen()

tim.speed("fastest")

scr.title("ETCH-A-SKETCH")
scr.bgcolor("white")


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def move_anticlockwise():
    tim.right(20)
    # tim.setheading(tim.heading() + 20)


def move_clockwise():
    tim.left(20)
    # tim.setheading(tim.heading() - 20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


scr.listen()
scr.onkeypress(key='w', fun=move_forwards)
scr.onkeypress(key='s', fun=move_backwards)
scr.onkeypress(key='a', fun=move_anticlockwise)
scr.onkeypress(key='d', fun=move_clockwise)
scr.onkey(key='c', fun=clear)

scr.exitonclick()
