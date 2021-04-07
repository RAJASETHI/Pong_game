from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle(x_pos=350, y_pos=0)
right_paddle = Paddle(x_pos=-350, y_pos=0)
screen.listen()
screen.onkeypress(left_paddle.up, "Up")
screen.onkeypress(left_paddle.down, "Down")

screen.onkeypress(right_paddle.up, "w")
screen.onkeypress(right_paddle.down, "s")

ball=Ball()

game_on = True
while game_on:
    screen.update()
screen.exitonclick()