from turtle import Turtle

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_dist = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in starting_pos:
            seg = Turtle("square")
            seg.color("green")
            seg.up()
            seg.goto(pos)
            self.segments.append(seg)

    def add_segment(self):
        seg = Turtle("square")
        seg.color("green")
        seg.up()
        seg.goto(self.segments[-1].position())
        self.segments.append(seg)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):    # start , stop , step
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.head.forward(move_dist)

    def reset(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
