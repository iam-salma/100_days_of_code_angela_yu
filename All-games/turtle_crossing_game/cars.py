import random
from turtle import Turtle
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("car.gif")
        self.up()
        self.goto(random.randint(-350, 350), random.randint(-250, 250))

    def move(self, lev):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE - (MOVE_INCREMENT * lev), self.ycor())
        if self.xcor() < -350:
            self.goto(350, random.randint(-250, 250))

