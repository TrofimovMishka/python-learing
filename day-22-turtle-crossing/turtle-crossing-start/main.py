import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

HEIGHT = 600

screen = Screen()
screen.setup(width=600, height=HEIGHT)
screen.tracer(0)
screen.listen()

count = 0
game_is_on = True

car_manager = CarManager()
turtle = Player()
score = Scoreboard(-230, 270)

screen.onkey(turtle.go_up, "w")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.print_score()
    count += 1

    car_manager.go()

    if count == 6:
        car_manager.add_car()
        car_manager.delete_unbound_cars(HEIGHT)
        count = 0

    if car_manager.detect_collision(turtle):
        game_is_on = False
        score.game_over()
        
    if turtle.is_return_to_start():
        car_manager.increase_speed()
        score.add_score()


screen.exitonclick()
