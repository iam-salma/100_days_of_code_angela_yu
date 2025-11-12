from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.up()
        self.x_dist = 3
        self.y_dist = 3
        self.speed = 0.1

    def move(self):
        x = self.xcor() + self.x_dist
        y = self.ycor() + self.y_dist
        self.goto(x, y)

    def bounce_wall(self):
        self.y_dist *= -1

    def bounce_paddle(self):
        self.x_dist *= -1
        self.move()

    def reset(self):
        self.goto(0, 0)
        self.speed = 0.1
