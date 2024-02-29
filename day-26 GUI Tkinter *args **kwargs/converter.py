from tkinter import *

win = Tk()
win.minsize(width=250, height=150)
win.title("Miles to KM converter")
win.config(padx=30, pady=30)


def calculate():
    mile = float(mile_input.get())
    km = mile * 1.609
    km_text.config(text=f'{km}')


mile_input = Entry(width=5)
mile_input.grid(column=1, row=0)

mile_label = Label(text='Miles')
mile_label.grid(column=2, row=0)

km_text = Label(text='0')
km_text.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)

is_equal = Label(text='is_equal')
is_equal.grid(column=0, row=1)

win.mainloop()
