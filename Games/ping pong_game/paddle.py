from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.7, stretch_wid=3)
        self.up()
        self.goto(pos)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
