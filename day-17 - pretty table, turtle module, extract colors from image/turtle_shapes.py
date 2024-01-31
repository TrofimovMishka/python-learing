from turtle import *
import random

# import turtle as t -> how set alias for module

screen = Screen()
screen.screensize(900, 900, "#26a69a")

john = Turtle()
john.shape("triangle")
john.color("#e0f2f1")
john.pencolor("#f4ff81")

john.speed(3)

# for i in range(4):
#     john.fd(100)
#     john.rt(90)
#     john.dot(10, "#ffd180")
#
# john.goto(0, 100)
# john.dot(10, "#ffd180")
#
#
# for i in range(15):
#     john.fd(10)
#     john.penup()
#     john.fd(10)
#     john.pendown()

r = random.Random()

sides = 3

while sides <= 9:
    angle = 360 / sides
    for _ in range(sides):
        john.fd(120)
        john.rt(angle)

    sides += 1

    john.pencolor(f"#{r.randint(100000, 900000)}")

screen.exitonclick()
