from turtle import Turtle, Screen

john = Turtle()
screen = Screen()


def move_fd():
    john.fd(10)


def move_bk():
    john.bk(10)


def move_rt():
    john.rt(15)


def move_lt():
    john.lt(15)


def move_home():
    john.home()


def clear():
    john.clear()
    john.penup()
    john.home()
    john.pendown()


screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bk)
screen.onkey(key="a", fun=move_lt)
screen.onkey(key="d", fun=move_rt)
screen.onkey(key="space", fun=move_home)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
