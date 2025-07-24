import turtle

tim = turtle.Turtle()
scr = turtle.Screen()

tim.color("gold")
tim.fillcolor("yellow")
scr.title("A SQUARE")
scr.bgcolor("teal")

# print(tim) o/p = <turtle.Turtle object at 0x000001C8A0CC08C0>
# tim.home

tim.begin_fill()

while True:
    tim.forward(100)
    tim.right(90)
    x, y = tim.pos()
    if abs(x) < 1 and abs(y) < 1:
        break
tim.end_fill()

scr.exitonclick()

# tim.home() sends the turtle to home(0, 0)
