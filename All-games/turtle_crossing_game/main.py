from turtle import *
from player import Player
from level import Level
from cars import Cars
import time

colormode(255)

scr = Screen()
scr.addshape("turtle.gif")
scr.addshape("car.gif")

player = Player()
level = Level()

scr.title("CHICKEN CROSSING THE ROAD")
scr.bgcolor("black")
scr.setup(height=700, width=700)
scr.tracer(0)

scr.listen()
scr.onkeypress(player.move_up, "Up")
scr.onkeypress(player.move_down, "Down")

car_array = []
for i in range(0, 10):
    car = Cars()
    car_array.append(car)

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    for car in car_array:
        car.move(level.level)
        if player.distance(car) < 15:
            level.game_over()
            game_is_on = False
    if player.ycor() >= 300:
        level.increase()
        player.reset()


scr.exitonclick()
