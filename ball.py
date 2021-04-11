from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.00000000001

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def collision_walls(self):
        self.move_y *= -1
        # self.fd(10)

    def collision_paddle(self):
        self.move_x *= -1
        # self.move_y *= -1
        self.move_speed *=2

    def reverse_ball(self):
        self.goto(0, 0)
        self.move_x *= -1
