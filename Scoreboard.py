from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, xnum, ynum):
        super().__init__()
        self.penup()
        self.goto(xnum, ynum)
        self.pencolor("white")
        self.hideturtle()
        self.score = 0
        self.printScore()

    def printScore(self):
        self.clear()
        self.write(f"{self.score}", False, "center", font=("Comic Sans MS", 40, "normal"))

    def increment(self):
        self.score += 1
        self.printScore()
