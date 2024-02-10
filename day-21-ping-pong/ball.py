import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(0.6, 0.6)

    def go(self):
        # x = self.xcor() + 3
        # y = self.ycor() + 3
        # self.goto(x, y)
        self.fd(6)

    def change_direction_during_wall_collision(self):
        h = self.heading()
        if 90 <= h <= 180:
            new_h = 180 - h
            self.setheading(180 + new_h)
        elif 180 <= h <= 270:
            new_h = h - 180
            self.setheading(180 - new_h)
        elif 0 <= h <= 90:
            self.setheading(360 - h)
        elif 270 <= h <= 360:
            self.setheading(360 - h)

    def change_direction_during_paddle_collision(self):
        h = self.heading()
        if 90 <= h <= 180:
            new_h = 180 - h
            self.setheading(new_h)
        elif 180 <= h <= 270:
            new_h = h - 180
            self.setheading(360 - new_h)
        elif 0 <= h <= 90:
            new_h = 90 - h
            self.setheading(90 + new_h)
        elif 270 <= h <= 360:
            new_h = 360 - h
            self.setheading(180 + new_h)

    def random_direction(self):
        self.setheading(random.randint(120, 250))
