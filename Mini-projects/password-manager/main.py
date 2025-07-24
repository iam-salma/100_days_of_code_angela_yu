from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import json
import pyperclip

# ---------------------------- FIND PASSWORD ------------------------------- #

def search_data():
    website = web_inp.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="file not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=web_inp.get(), message=f"\nEmail:{email}\nPassword:{password}")
        else:
            messagebox.showerror(title="ERROR", message="website no found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_pass():
    pass_inp.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = ([choice(letters) for _ in range(randint(8, 10))] + [choice(symbols) for _ in range(randint(2, 4))]
                        + [choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)
    pass_inp.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_inp.get()
    email = e_inp.get()
    password = pass_inp.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showerror(title="OOPS!", message="Please fill all the fields!")
    else:
        # is_ok = messagebox.askokcancel(title=web_inp.get(), message=f"These are the details entered:"
        #                                                             f"\nEmail:{email}\nPassword:{password}"
        #                                                             f"\nWould you like to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # reading the new data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating the existing data with the new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)          # data.write(f"{website} | {email} | {password}")
        finally:
            web_inp.delete(0, END)
            e_inp.delete(0, END)
            pass_inp.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_txt = Label(text="Website: ", font=("ariel", 13))
website_txt.grid(column=0, row=1)
web_inp = Entry(width=34)
web_inp.grid(column=1, row=1)               # web_inp.place(x=143, y=202)
search = Button(text="Search", width=14, command=search_data)
search.grid(column=2, row=1)

email_txt = Label(text="Email/Username: ", font=("ariel", 13))
email_txt.grid(column=0, row=2)
e_inp = Entry(width=53)
e_inp.grid(column=1, row=2, columnspan=2)   # e_inp.place(x=143, y=227)

password_txt = Label(text="Password: ", font=("ariel", 13))
password_txt.grid(column=0, row=3)
pass_inp = Entry(width=34)
pass_inp.grid(column=1, row=3)              # pass_inp.place(x=143, y=252)
genpass = Button(text="Generate Password", command=random_pass)
genpass.grid(column=2, row=3)               # genpass.place(x=355, y=252)

add = Button(text="Add", width=45, command=save)
add.grid(column=1, row=5, columnspan=2)     # add.place(x=143, y=280)

window.mainloop()
