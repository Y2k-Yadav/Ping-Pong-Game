from turtle import Turtle, Screen
from paddle import Paddle

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
screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()

