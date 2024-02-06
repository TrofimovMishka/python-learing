from turtle import Turtle

RIGHT = 0
LEFT = 180
DOWN = 270
UP = 90

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20


class Snake:
    def __init__(self):
        self.is_live = True
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in START_POSITIONS:
            snake_item = Turtle(shape="square")
            snake_item.penup()
            snake_item.heading()
            snake_item.color("white")
            snake_item.goto(i)
            self.segments.append(snake_item)

    def go(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.head.fd(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
