from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.color("green")
        self.shape("square")
        self.turtlesize(4, 0.5)
        self.speed("fastest")

    def up(self):
        if self.ycor() <= 340:
            self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        if self.ycor() >= -340:
            self.goto(self.xcor(), self.ycor()-20)
