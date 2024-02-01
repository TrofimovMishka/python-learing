import random
import turtle as t

screen = t.Screen()
screen.setup(1600, 1000)
user_choice = screen.textinput(title="Make your bet", prompt="Which will win? Enter a color: ")  # User input on screen

# Can be refactored with list of turtles that will be created with for i in range and added to list, then in for loop
# - start all. Create list of colors, create list of x and y positions and use john.goto(-700, 400)

john = t.Turtle(shape="turtle")
bob = t.Turtle(shape="turtle")
jorge = t.Turtle(shape="turtle")
alice = t.Turtle(shape="turtle")

john.penup()
john.goto(-700, 400)
john.color("red", "red")
john.pensize(5)
john.pendown()

bob.penup()
bob.goto(-700, 300)
bob.color("brown", "brown")
bob.pensize(5)
bob.pendown()

jorge.penup()
jorge.goto(-700, 200)
jorge.color("yellow", "yellow")
jorge.pensize(5)
jorge.pendown()

alice.penup()
alice.goto(-700, 100)
alice.color("purple", "purple")
alice.pensize(5)
alice.pendown()

rnd = random.Random()

is_run = True


def start():
    global is_run
    is_run = True
    while is_run:
        john.fd(rnd.randint(0, 10))
        bob.fd(rnd.randint(0, 10))
        jorge.fd(rnd.randint(0, 10))
        alice.fd(rnd.randint(0, 10))


def pause():
    global is_run
    is_run = not is_run


screen.listen()
screen.onkey(key="space", fun=start)
screen.onkey(key="p", fun=pause)

screen.exitonclick()
