THEME_COLOR = "#375362"

from tkinter import *


class UserInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.configure()
        self.window.mainloop()

    def configure(self):
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(anchor="w", text="Score: 0", bg=THEME_COLOR, highlightthickness=0,
                           font=('Arial', 13, "bold"), fg='white')
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)

        self.question = self.canvas.create_text(150, 125,
                                                text='All data provided by the API is available under the Creative Commons',
                                                fill='black', font=("Arial", 20, "italic"), anchor=NW, justify="center")
        # The anchor parameter controls the positioning of an item in terms of its coordinates.
        # The default value is CENTER (so using this puts the center of the text at the coordinates (50, 0) in the earlier example),
        # but you can also use NW, N, NE (effectively top-left, top-middle, top-right), W, E (left and right),
        # and SW, S, SE (bottom-left, bottom-middle, bottom-right).
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)

        self.yes_photo = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=self.yes_photo, highlightthickness=0, command=self.true_action)
        self.yes_button.grid(column=0, row=2)

        self.no_photo = PhotoImage(file="images/false.png")
        self.no_button = Button(image=self.no_photo, highlightthickness=0, command=self.false_action)
        self.no_button.grid(column=1, row=2)

    def true_action(self):
        pass

    def false_action(self):
        pass
