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
            snake_item = self.create_segment()
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

    def grow(self):
        snake_item = self.create_segment()
        snake_item.goto(self.segments[-1].position())
        self.segments.append(snake_item)

    def create_segment(self):
        snake_item = Turtle(shape="square")
        snake_item.penup()
        snake_item.heading()
        snake_item.color("white")
        return snake_item

    def is_head_collision(self, x, y):
        # Collision with wall
        if self.head.xcor() > x or self.head.xcor() < -x or self.head.ycor() > y or self.head.ycor() < -y:
            self.is_live = False
            return True
        # Solution with slicing: [from:to:step] - [::2] - from start, to the end each second; [::-1] - revers list
        # Slicing work with list, tuples, string. [1:] - from 1 to the end

        # Collision with tail
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                self.is_live = False
                return True

        return False
