# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_check.config(text="")
    reps = 0
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    minutes = f"{count // 60:02d}"
    seconds = f"{count % 60:02d}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps % 2):
            mark += "✔"
        label_check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

# window.after(1000, my_method, "Hello") # how long wait and after do something. 1000 - ms to wait, my_method - method to triger, "Hello" - argument for this method can a lot of


tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

canvas.create_image(100, 112, image=tomato_image)  # set position for image
timer_text = canvas.create_text(100, 132, text='00:00', fill='black', font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

label_check = Label(fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=3)

label_timer = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
label_timer.grid(column=1, row=0)

button_start = Button(text='Start', highlightthickness=0, background=GREEN, activebackground=YELLOW,
                      command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', highlightthickness=0, background=GREEN, activebackground=RED, command=reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()
