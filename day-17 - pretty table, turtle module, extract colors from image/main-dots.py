import random
import turtle as t
from turtle import Screen

import colorgram

rand = random.Random()

screen = Screen()
screen.screensize(600, 600, "#f7faf8")

john = t.Turtle()
t.colormode(255)  # Allow you to use random color
t.screensize(600, 600)
john.shape("turtle")
john.pensize(50)
john.pencolor("#fcdf03")
john.color("#7b947e")

john.speed(15)
john.penup()
john.hideturtle()

# col = colorgram.extract('image.jpg', 50)

colors = [(241, 239, 240), (239, 236, 227), (228, 236, 242), (201, 164, 116), (230, 219, 84), (229, 240, 235), (210, 63, 107), (231, 73, 43), (164, 51, 76), (61, 81, 142), (161, 74, 49), (113, 179, 207), (212, 139, 169), (60, 48, 129), (62, 36, 59), (112, 41, 72), (51, 141, 96), (156, 160, 58), (106, 45, 43), (41, 43, 65), (48, 185, 168), (225, 168, 208), (123, 227, 223), (82, 105, 205), (67, 36, 31), (166, 177, 223), (117, 184, 166), (131, 217, 224), (231, 172, 164), (238, 208, 14), (16, 107, 98), (75, 158, 167), (36, 81, 83)]

# for i in colorgram.extract('image.jpg', 50):
#     colors.append((i.rgb.r, i.rgb.g, i.rgb.b))

john.setheading(225)
john.fd(600)
john.setheading(0)

def left():
    john.lt(90)
    john.fd(40)
    john.lt(90)
    john.fd(40)

def go():
    for _ in range(20):
        john.dot(15, rand.choice(colors))
        john.fd(40)

def right():
    john.rt(90)
    john.fd(40)
    john.rt(90)
    john.fd(40)


i = 0

while i < 20:
    i += 2
    go()
    left()
    go()
    right()


# Solution form lesson:

# number_of_dots = 100
# for dot_count in range(1, number_of_dots):
#     john.dot(20, rand.choice(colors))
#     john.forward(50)
#
#     if dot_count % 10 == 0:
#         john.setheading(90)
#         john.forward(50)
#         john.setheading(180)
#         john.forward(500)
#         john.setheading(0)

screen.exitonclick()
