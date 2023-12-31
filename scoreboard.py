from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-60, 220)
        self.write(self.score_left, align="CENTER", font=("courier", 60, "normal"))
        self.goto(60, 220)
        self.write(self.score_right, align="CENTER", font=("courier", 60, "normal"))

    def updatescore_left(self):
        self.score_left += 1
        self.updatescore()
    def updatescore_right(self):
        self.score_right += 1
        self.updatescore()
