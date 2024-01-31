import random
import turtle as t
from turtle import Screen

rand = random.Random()

screen = Screen()
screen.screensize(600, 600, "#e0ffe4")

john = t.Turtle()
t.colormode(255)  # Allow you to use random color
john.shape("triangle")
john.pencolor("#fcdf03")
john.color("#7b947e")

john.speed(13)


def get_random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)

    return r, g, b


while john.heading() < 350:
    john.circle(150)
    # john.rt(10) # my solution
    john.setheading(john.heading() + 10) # solution from lesson
    john.pencolor(get_random_color())


screen.exitonclick()
