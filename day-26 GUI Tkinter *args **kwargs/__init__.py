from tkinter import *

window = Tk()
window.title("GUI App from PY")
window.minsize(width=900, height=900)

# label:
label = Label(text="Registration... ", font=('Arial', 30, "bold"))
# label.pack(side="left") # place into a screen left side
label.pack(expand=True) # place into a screen center

# Configure, change and update component:
label["text"] = "Updated label"
# OR:
label.config(text="Updated label2")

var = 0
def button_update():
    global var
    print("Button clicked")
    # var += 1
    label.config(text=f"Button was clicked...{input.get()}")

# tkinter components:

# Button
button = Button(background="yellow", text="Update", font=('Arial', 5, "bold"), command=button_update) # important method without ()!!!!!
button.pack(expand=True)

# Input zone
input = Entry(width=50)
input.insert(END, "Placeholder text")
input.pack(expand=True)

# Multi line Text
text =Text(height=10, width=50)
text.focus() # put cursor to text
text.insert(END, "Text placeholder")

print(text.get("1.0", END)) # get current value at line 1, char 0 (1.0)

text.pack(expand=True)

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width= 5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbox:
def checkbox_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbutton.pack()

# Radiobutton:
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton_1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton_2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

radiobutton_1.pack()
radiobutton_2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["a", "b", "c"]

for i in fruits:
    listbox.insert(fruits.index(i), i)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
