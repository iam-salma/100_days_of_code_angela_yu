import turtle


def fxn(x, y):
    turtle.ondrag(None)
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    turtle.ondrag(fxn)


turtle.speed(10)

sc = turtle.Screen()
sc.setup(400, 300)
turtle.ondrag(fxn)


sc.mainloop()
