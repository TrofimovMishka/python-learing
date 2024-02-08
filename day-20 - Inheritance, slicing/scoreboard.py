from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", align="center", font=('Courier', 15, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER. Your score = {self.score}", align="center", font=('Courier', 25, 'normal'))

    def add_score(self):
        self.clear()
        self.score += 1
        self.print_score()
