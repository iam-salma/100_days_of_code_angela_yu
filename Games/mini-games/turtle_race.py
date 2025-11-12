import random
from turtle import *

scr = Screen()
scr.setup(height=400, width=500)
scr.title("TURTLE RACE")
scr.bgcolor("black")
bet = scr.textinput(title="PLACE A BET!", prompt="choose the color of the turtle that will win: ")

is_race_on = False
colors = ["red", "blue", "purple", "green", "orange", "gold"]
all_turtles = []
y_pos = 150

for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.up()
    turtle.goto(x=-230, y=y_pos)
    all_turtles.append(turtle)
    y_pos -= 50

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            win = turtle.pencolor()     # always mention pencolor to get the color of turtle
            if win == bet:
                print(f"You've won! The {win} turtle is the winner!")
            else:
                print(f"You've lost! The {win} turtle is the winner!")
            is_race_on = False
        turtle.forward(random.randint(1, 6))

scr.exitonclick()
