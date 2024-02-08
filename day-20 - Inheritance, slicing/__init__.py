import time
import turtle as t

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")

screen.tracer(0)  # off blinking of screen

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while snake.is_live:
    screen.update()
    time.sleep(0.1)
    snake.go()

    # Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.add_score()

    if snake.is_head_collision(280, 280):
        scoreboard.game_over()

screen.exitonclick()
