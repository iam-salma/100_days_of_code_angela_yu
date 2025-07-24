from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("apple.gif")
        self.up()
        self.shapesize(0.65, 0.65)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-370, 370), random.randint(-370, 340))
