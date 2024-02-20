import pandas
from turtle import Screen
import turtle

STATES_CSV = "50_states.csv"
PICNAME = "blank_states_img.gif"
FONT = ("Courier", 9, "bold")

screen = Screen()
screen.setup(width=750, height=510)
screen.title("USA Game")
screen.addshape(PICNAME)
# screen.bgpic(PICNAME)

turtle.shape(PICNAME)

# place the text in coordinate:
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor) # return coordinate where mouse click

states = pandas.read_csv(STATES_CSV)
is_game = True


def write_state():
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.write(f"{state}", align="center", font=FONT)

while is_game:
    user_answer = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

    if user_answer == 'Exit':
        is_game = False
        break

    row = states[states.state == user_answer]

    if row.empty:
        is_game = False
        break
    else:
        x = row.x.item() # similar to x = row.x.values[0]
        y = row.y.item()
        state = row.state.item()

        write_state()

# turtle.mainloop() # infinite open window
