import json
from tkinter import *
from tkinter import messagebox

import pyperclip

import password_generator

PASSWORDS_TXT = "my_passwords.txt"

DEFAULT_EMAIL = "user@example.mail"

PAD = 7

BLACK = '#000000'
GRAY = '#CCCCCC'
GREEN = '#007f00'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password = password_generator.get_password()
    input_password.insert(END, password)
    pyperclip.copy(password)  # how add this line to copy buffer - than you can use Ctrl+V to paste it


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    web = input_website.get()
    username = input_username.get()
    password = input_password.get()

    result = f'{web} | {username} | {password} \n'
    # How create a json (dictionary):
    new_data = {
        web: {
            "email": username,
            "password": password
        }
    }

    if len(web) < 1 or len(password) < 1:
        messagebox.showwarning("Ooops", "Please don't leave any empty fields")
    else:
        # is_ok = messagebox.showinfo(f"Save for {web}",
        #                             f"Your really want to save: \n Email: {username} \n Password: {password}")
        # if is_ok:
        # with open("my_passwords.txt", mode="a") as file:
        #     # file.write(result)
        #     json.dump(new_data, file, indent=4)  # use json module to write json to file;
        #     # indent=4 => make pretty formatted json view
        #     input_website.delete(0, END)
        #     input_password.delete(0, END)

        # with open("my_passwords.txt", mode="r") as file:
        #     data_from_file = json.load(file)  # how read data with json module
        #     print(data_from_file)

        try:
            with open(PASSWORDS_TXT, mode="r") as file:
                data_from_file = json.load(file)
        except FileNotFoundError:
            with open(PASSWORDS_TXT, mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # This work only if file exist and !!!!!! HAVE JSON DATA !!!!!!
            data_from_file.update(new_data)  # how UPDATE data with json module
            with open(PASSWORDS_TXT, mode="w") as data_file:  # This add data to file like next json object
                json.dump(data_from_file, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- Search ------------------------------- #

def search():
    web = input_website.get()
    try:
        with open(PASSWORDS_TXT, mode="r") as file:
            data_from_file = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data")
    else:
        if web in data_from_file:
            data = data_from_file[web]

            email = data["email"]
            password = data["password"]

            messagebox.showinfo(title=web, message=f"Email: {email}, password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exist")


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

input_website = Entry(width=25, bg=GRAY, highlightthickness=0)
input_website.grid(column=1, row=1, columnspan=2)
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

search_button = Button(text="Search", highlightthickness=0, pady=-1, background=GRAY,
                       command=search, width=16)
search_button.grid(column=3, row=1)

window.mainloop()
