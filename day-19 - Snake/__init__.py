import time
import turtle as t

from snake import Snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")

screen.tracer(0)  # off blinking of screen

snake = Snake()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while snake.is_live:
    screen.update()
    time.sleep(0.25)
    snake.go()

screen.exitonclick()
