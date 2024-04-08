THEME_COLOR = "#375362"

from tkinter import *

from quiz_brain import QuizBrain


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):  # typed params: quiz_brain: QuizBrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.configure()
        self.get_next_question()
        self.window.mainloop()

    def configure(self):
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(anchor="w", text="Score: 0", bg=THEME_COLOR, highlightthickness=0,
                           font=('Arial', 13, "bold"), fg='white')
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)

        self.question = self.canvas.create_text(150, 125, width=280,
                                                text='All data provided by the API is available under the Creative Commons',
                                                fill='black', font=("Arial", 20, "italic"), justify="center")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)

        self.yes_photo = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=self.yes_photo, highlightthickness=0, command=self.true_action)
        self.yes_button.grid(column=0, row=2)

        self.no_photo = PhotoImage(file="images/false.png")
        self.no_button = Button(image=self.no_photo, highlightthickness=0, command=self.false_action)
        self.no_button.grid(column=1, row=2)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            self.q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=self.q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz!")
            self.yes_button.config(state="disabled") # How disable element in screen
            self.no_button.config(state="disabled")

    def true_action(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback(is_true)

    def false_action(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback(is_false)

    def change_to_red(self):
        self.canvas.config(background="red")

    def change_to_green(self):
        self.canvas.config(background="green")

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
