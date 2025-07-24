from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=20)

txt1 = Label(text='is equal to')
txt1.grid(column=1, row=2)
txt2 = Label(text='miles')
txt2.grid(column=3, row=1)
txt3 = Label(text='km')
txt3.grid(column=3, row=2)
txt4 = Label(text='0')
txt4.grid(column=2, row=2)

input = Entry(width=10)
input.grid(column=2, row=1)


def button_clicked():
    txt4.config(text=int(input.get())*1.6)


button = Button(text="calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()
