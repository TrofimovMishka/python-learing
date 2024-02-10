import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Ping - Pong")
screen.tracer(0)  # off blinking of screen

paddle_r = Paddle(580, 0)
paddle_l = Paddle(-580, 0)
paddle_l.color("blue")
ball = Ball()
scoreboard = Scoreboard(0, 350)
scoreboard_r = Scoreboard(180, 350)
scoreboard_l = Scoreboard(-180, 350)
scoreboard.clear()

screen.listen()

screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

screen.onkey(paddle_r.up, "i")
screen.onkey(paddle_r.down, "k")

not_down = True
is_ball_hit_wall_up = False
is_ball_hit_wall_down = False

is_game_over = False
ball.random_direction()


def move_r_paddle():
    global not_down
    if paddle_r.ycor() > 340:
        not_down = False
    if paddle_r.ycor() < -340:
        not_down = True
    if not_down:
        paddle_r.up()
    if not not_down:
        paddle_r.down()


def detect_paddle_ball_contact():
    if ball.distance(paddle_r) < 50 and ball.xcor() > 560:
        ball.change_direction_during_paddle_collision()
        scoreboard_r.add_score()
    elif ball.distance(paddle_l) < 50 and ball.xcor() < -560:
        ball.change_direction_during_paddle_collision()
        scoreboard_l.add_score()


def detect_ball_wall_contact():
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.change_direction_during_wall_collision()


def detect_ball_missing():
    global is_game_over
    if ball.xcor() > 590 or ball.xcor() < -590:
        is_game_over = True
        scoreboard.game_over()


while not is_game_over:
    screen.update()
    time.sleep(0.02)

    scoreboard_r.print_score()
    scoreboard_l.print_score()

    detect_paddle_ball_contact()
    detect_ball_wall_contact()
    detect_ball_missing()
    # move_r_paddle()

    ball.go()

screen.exitonclick()
