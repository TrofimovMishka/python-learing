import random
import turtle as t
from turtle import Screen

# import turtle as t -> how set alias for module

screen = Screen()
screen.screensize(600, 600, "#26a69a")

john = t.Turtle()
t.colormode(255) # Allow you to use random color
john.shape("triangle")
john.color("#e0f2f1")
john.pencolor("#f4ff81")
john.width(15)

john.speed(2)

rand = random.Random()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

tup = (1, 2, 4, 90)  # this is the tuple - immutable collection in py


def get_random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)

    return r, g, b


while True:
    john.fd(40)
    john.rt(rand.randint(1, 4) * 90)
    # john.pencolor(rand.choice(colours))
    john.pencolor(get_random_color())

screen.exitonclick()
