from tkinter import *
from tkinter import messagebox

import password_generator

DEFAULT_EMAIL = "user@example.mail"

PAD = 7

BLACK = '#000000'
GRAY = '#CCCCCC'
GREEN = '#007f00'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    input_password.insert(END, password_generator.get_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    web = input_website.get()
    username = input_username.get()
    password = input_password.get()

    result = f'{web} | {username} | {password} \n'

    if len(web) < 1 or len(password) < 1:
        messagebox.showwarning("Ooops", "Please don't leave any empty fields")
    else:
        is_ok = messagebox.showinfo(f"Save for {web}",
                                    f"Your really want to save: \n Email: {username} \n Password: {password}")
        if is_ok:
            with open("my_passwords.txt", mode="a") as file:
                file.write(result)
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password generator")
window.config(padx=40, pady=40, bg=BLACK)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
image = canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

web_site_label = Label(text="Website:", bg=BLACK, fg=GRAY, padx=PAD, pady=PAD)
web_site_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", bg=BLACK, fg=GRAY, padx=PAD, pady=PAD)
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:", bg=BLACK, fg=GRAY, padx=PAD, pady=PAD)
pass_label.grid(column=0, row=3)

input_website = Entry(width=45, bg=GRAY, highlightthickness=0)
input_website.grid(column=1, row=1, columnspan=3)
input_website.focus()  # set cursor to this

input_username = Entry(width=45, bg=GRAY, highlightthickness=0)
input_username.grid(column=1, row=2, columnspan=3)
input_username.insert(END, DEFAULT_EMAIL)

input_password = Entry(width=26, bg=GRAY, highlightthickness=0)
input_password.grid(column=1, row=3)

generate_button = Button(text="Generate Password", highlightthickness=0, pady=-1, background=GREEN,
                         command=generate_pass)
generate_button.grid(column=3, row=3)

add_button = Button(text="Add", width=43, highlightthickness=0, pady=-3, command=add_pass)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()
