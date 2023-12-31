from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        # x = self.xcor() + 1    we can make it move 1 pixel every time that means we can get an extra time were we can
        # get the time to hit the ball.  when ever loop runs it will move with 1 pixel
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)


    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
