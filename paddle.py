from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
