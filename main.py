from turtle import Turtle, Screen
import time

from Scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

left_paddle = Paddle(x_pos=-350, y_pos=0)
right_paddle = Paddle(x_pos=350, y_pos=0)
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
Score2 = Scoreboard(250, 230)
Score1 = Scoreboard(-250, 230)
ball = Ball()
game_on = True
while game_on:
    time.sleep(abs(0.1-ball.move_speed))
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision_walls()
    if 320 < ball.xcor() < 350 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(
            left_paddle) < 50:
        ball.collision_paddle()
        # print("Made Contact!!")
    if ball.xcor() > 400:
        # game_on = False
        ball.reverse_ball()
        Score1.increment()

    if ball.xcor() < -400:
        ball.reverse_ball()
        Score2.increment()
screen.exitonclick()
