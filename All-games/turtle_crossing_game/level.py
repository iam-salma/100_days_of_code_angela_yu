from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(-250, 300)
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("ariel", 20, "bold"))

    def increase(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("ariel", 20, "bold"))
