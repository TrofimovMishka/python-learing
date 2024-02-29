from tkinter import *

window = Tk()
window.title("GUI App from PY")
window.minsize(width=900, height=900)
window.config(padx=20, pady=20) # how add padding from border

# label:
label = Label(text="Registration... ", font=('Arial', 30, "bold"))
# label.pack(side="left") # place into a screen left side
# Configure, change and update component:
label["text"] = "Updated label"
# OR:
label.config(text="Updated label2")
# label.pack(expand=True) # place into a screen center

# How precise place elements on window:
# label.place(x=10, y=12)

# Grid layout manager - work with columns and rows (start from 0): pack and grid not compatible and can't use together
label.config(padx=20, pady=20) # how add padding to elements
label.grid(column=0, row=1)


var = 0
def button_update():
    global var
    print("Button clicked")
    # var += 1
    label.config(text=f"Button was clicked...{input.get()}")

# tkinter components:

# Button
button = Button(background="yellow", text="Update", font=('Arial', 5, "bold"), command=button_update) # important method without ()!!!!!
# button.pack(expand=True)
button.grid(column=0, row=2)

# Input zone
input = Entry(width=50)
input.insert(END, "Placeholder text")
input.grid(column=1, row=1)
# input.pack(expand=True)


window.mainloop()