from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
    # def __init__(self,x,y): using seperate argument not tuple positional argument
        super().__init__( )
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        # self.turtlesize(5,2)
        self.penup()
        self.goto(position)
        #self.goto(x,y) this is by using two different argument when we are passing

    def up(self):
        y = self.ycor()
        self.goto(self.xcor(),(y + 20))

    def down(self):
        y = self.ycor()
        self.goto(self.xcor(), (y - 20))
