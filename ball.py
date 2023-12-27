from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
    def move(self):
        # x = self.xcor() + 1    we can make it move 1 pixel every time that means we can get an extra time were we can
        # get the time to hit the ball.  when ever loop runs it will move with 1 pixel
        x = self.xcor() + 10
        y = self.ycor() + 10
        self.goto(x,y)
