from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = ""
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

def reset_clicked():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(time, text="00:00")
    label.config(text="Timer")
    track.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_clicked():
    global reps
    reps += 1
    work_sec = WORK_MIN * 6
    break_sec = SHORT_BREAK_MIN * 6
    long_break_sec = LONG_BREAK_MIN * 6

    if reps % 8 == 0:
        label.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        countdown(break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(n):
    minute = n // 60
    sec = n % 60
    canvas.itemconfig(time, text=f"{minute:02}:{sec:02}")
    if n > 0:
        global timer
        timer = window.after(1000, countdown, n-1)
    else:
        start_clicked()
        marks = ""
        for _ in range(reps//2):
            marks += "✓"
        track.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label.grid(column=2, row=1)

canvas = Canvas(height=250, width=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.gif")
canvas.create_image(103, 112, image=img)
time = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start = Button(text="Start", width=6, bg=GREEN, command=start_clicked)
start.grid(column=1, row=5)

track = Label(fg=GREEN, bg=YELLOW, font=("ariel", 30, "bold"))
track.grid(column=2, row=6)

reset = Button(text="Reset", width=6, bg=GREEN, command=reset_clicked)
reset.grid(column=3, row=5)

window.mainloop()
