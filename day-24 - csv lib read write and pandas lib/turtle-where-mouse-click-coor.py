import pandas
from turtle import Screen
import turtle

PICNAME = "usa_game/blank_states_img.gif"

screen = Screen()
screen.setup(width=750, height=510)
screen.title("USA Game")
screen.addshape(PICNAME)
# screen.bgpic(PICNAME)

turtle.shape(PICNAME)

# place the text in coordinate:
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor) # return coordinate where mouse click


turtle.mainloop() # infinite open window