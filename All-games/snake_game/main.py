from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

scr = Screen()

scr.addshape("apple.gif")

snake = Snake()
food = Food()
score = Scoreboard()

scr.setup(height=800, width=800)
scr.title("SNAKE GAME")
scr.bgcolor("black")
scr.tracer(0)

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.right, "Right")
scr.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.add_segment()
        score.increase()

    # Detect collision with wall.
    if snake.head.xcor() > 399 or snake.head.xcor() < -399 or snake.head.ycor() > 399 or snake.head.ycor() < -399:
        score.reset()
        snake.reset()

    # Detect collision with tail.
    for seg in snake.segments:
        if seg == snake.head:
            snake.head.color("dark green")
        elif snake.head.distance(seg) < 15:
            score.reset()
            snake.reset()

scr.exitonclick()
