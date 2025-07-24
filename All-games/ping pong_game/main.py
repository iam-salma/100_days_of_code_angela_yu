from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

scr = Screen()
scr.title("PING-PONG GAME")
scr.bgcolor("black")
scr.setup(width=1200, height=700)
scr.tracer(0)

r_paddle = Paddle((-550, 0))
l_paddle = Paddle((550, 0))
score = Scoreboard()
ball = Ball()

scr.listen()
scr.onkey(r_paddle.go_up, "Up")
scr.onkey(r_paddle.go_down, "Down")
scr.onkey(l_paddle.go_up, "w")
scr.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    scr.update()
    ball.move()
    time.sleep(0.05)

    # Detect collision with wall
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.bounce_wall()

    # Detect collision with paddle
    if (ball.distance(l_paddle) < 50 and ball.xcor() > 550
            or ball.distance(r_paddle) < 50 and ball.xcor() < -550):
        ball.bounce_paddle()

    # Detect R paddle misses
    if ball.xcor() > 550:
        score.l_point()
        ball.reset()
        game_is_on = False

    # Detect L paddle misses:
    if ball.xcor() < -550:
        score.r_point()
        ball.reset()
        game_is_on = False

scr.exitonclick()
