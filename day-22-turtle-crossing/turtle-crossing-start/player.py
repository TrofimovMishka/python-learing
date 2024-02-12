STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self, shape="turtle", undobuffersize=1000, visible=True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def is_return_to_start(self):
        if self.ycor() > 290:
            self.goto(STARTING_POSITION)
            return True
        return False
