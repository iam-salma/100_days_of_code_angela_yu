from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
random_card = {}
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    org_data = pandas.read_csv("data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ----------------------------------- LOGIC ------------------------------------ #
def flip():
    canvas.itemconfig(front, image=back_img)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=random_card["English"], fill="white")

def next_card():
    global random_card, flip_timer
    window.after_cancel(flip_timer)
    random_card = choice(to_learn)
    canvas.itemconfig(front, image=front_img)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=random_card["French"], fill="black")
    flip_timer = window.after(5000, flip)

def is_known():
    to_learn.remove(random_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------------- UI SETUP --------------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=550, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
front = canvas.create_image(400, 280, image=front_img)
lang = canvas.create_text(400, 100, font=("ariel", 40, "bold"))
word = canvas.create_text(400, 280, font=("ariel", 50, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_img, bg=BACKGROUND_COLOR, border=0, command=next_card)
wrong.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right = Button(image=right_img, bg=BACKGROUND_COLOR, border=0, command=is_known)
right.grid(column=1, row=1)

flip_timer = window.after(3000, flip)
next_card()

window.mainloop()
