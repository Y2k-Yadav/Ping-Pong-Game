from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

turtle = Turtle()
screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
turtle.hideturtle()
screen.tracer(0)
right_paddle = Paddle((350,0))
# right_paddle = Paddle((350,0))  using tuple making it positional argument goto(x,y)
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
game_is_on = True

while game_is_on:
    # if we use time class it is importent to use
    # otherwise we dont use time method we can update therough while loop moving 1 pixel
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect the wall to the ball
    if ball.ycor() > 280  or ball.ycor() < -280:
        ball.bounce_y()

    #detect ball colled with paddle and edge of the paddle
    if  ball.distance(right_paddle) < 60 and ball.xcor() > 320  or ball.distance(left_paddle) < 60 and ball.xcor() < -320 :
        ball.bounce_x()


    #Detect ball will miss the paddle and change the direction
    if ball.xcor() >  380:
        ball.reset_position()
        scoreboard.updatescore_left()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.updatescore_right()


screen.exitonclick()

