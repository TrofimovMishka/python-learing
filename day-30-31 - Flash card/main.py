BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

import random
from tkinter import *

import pandas

timer = None


def get_data_to_learn():
    try:
        return pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
    except FileNotFoundError:
        print("File words_to_learn.csv no exist - default file will be open")
        return pandas.read_csv("data/french_words.csv").to_dict(orient="records")


data_to_learn = get_data_to_learn()
current_card = random.choice(data_to_learn)


def ok_action():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(data_to_learn)
    canvas.itemconfig(canvas_image, image=fr_image_url)

    canvas.itemconfig(language_text, text="French", fill='black')
    canvas.itemconfig(word_text, text=current_card["French"], fill='black')

    flip_timer = window.after(3000, flip_card)

    card_known()
    run_timer(3)


def nok_action():
    canvas.itemconfig(canvas_image, image=en_image_url)

    canvas.itemconfig(language_text, text="English", fill='white')
    canvas.itemconfig(word_text, text=current_card["English"], fill='white')


def run_timer(count):
    global timer

    canvas.itemconfig(timer_text, text=f"{count}")
    if count > 0:
        timer = window.after(1000, run_timer, count - 1)



def flip_card():
    global current_card

    canvas.itemconfig(canvas_image, image=en_image_url)
    canvas.itemconfig(language_text, text="English", fill='white')
    canvas.itemconfig(word_text, text=current_card["English"], fill='white')


def card_known():
    data_to_learn.remove(current_card)

    to_learn = pandas.DataFrame(data_to_learn)
    to_learn.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("FR - EN cards")
window.minsize(width=900, height=750)
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

fr_image_url = PhotoImage(file="images/card_front.png")
en_image_url = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(450, 300, image=fr_image_url)
language_text = canvas.create_text(450, 200, text='French', fill='black', font=(FONT_NAME, 30, "italic"))
word_text = canvas.create_text(450, 350, text=f"{current_card['French']}", fill='black', font=(FONT_NAME, 80, "bold"))
timer_text = canvas.create_text(450, 100, text='3', fill='gray', font=("Helvetica", 30, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

ok_button_url = PhotoImage(file="images/right.png")
nok_button_url = PhotoImage(file="images/wrong.png")

ok_button = Button(image=ok_button_url, highlightthickness=0, command=ok_action)
ok_button.grid(column=1, row=1)

nok_button = Button(image=nok_button_url, highlightthickness=0, command=nok_action)
nok_button.grid(column=0, row=1)

run_timer(3)
flip_timer = window.after(3000, flip_card)

window.mainloop()
