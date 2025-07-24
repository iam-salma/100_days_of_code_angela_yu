from turtle import Turtle
ALIGN = "center"
FONT = ("Ariel", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode='w') as file:
            file.write("0")
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.shape("square")
        self.color("white")
        self.up()
        self.hideturtle()
        self.goto(0, 350)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", font=FONT, align=ALIGN)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                self.write(f"{self.highscore}")
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", font=FONT, align=ALIGN)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()
