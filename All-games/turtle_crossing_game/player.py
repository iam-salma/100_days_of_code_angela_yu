from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle.gif")
        self.color("white")
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.setheading(90)
        self.up()
        self.goto(0, -300)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

    def reset(self):
        self.goto(0, -300)
