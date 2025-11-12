import turtle
import pandas

scr = turtle.Screen()
txt = turtle.Turtle()
txt.hideturtle()
txt.up()
img = "blank_states_img.gif"
scr.title("US States Game")
scr.setup(725, 491)
scr.addshape(img)
turtle.shape(img)

# def coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(coordinates)
# turtle.mainloop()

answered = []
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
# x = data.x.to_list()
# y = data.y.to_list()

game_is_on = True
while game_is_on:
    answer = scr.textinput(title=f"{len(answered)}/50 States guessed right",
                           prompt="whats the name of the other state?").title()
    if answer in states and answer not in answered:
        answered.append(answer)
        info = data[data.state == answer]       # index = states.index(answer)
        txt.goto(info.x.item(), info.y.item())  # txt.goto(x[index], y[index])
        txt.write(answer)
        data = data.drop(info.index)            # data = data[data.state != answer]
    elif answer in answered:
        continue
    else:
        txt.goto(0, 0)
        txt.write(f"Your guess was wrong ! Score = {len(answered)}/50", align="center", font=("Aerial", 20, "normal"))
        game_is_on = False
        scr.exitonclick()

# for state in states:
    # if state not in answered:
        # missing_states.append(state)
# new_data = pandas.dataframe(missing_states)
# new_data.to_csv("states.missed.csv")

data.to_csv("states.missed.csv")
turtle.mainloop()
