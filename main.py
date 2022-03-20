from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
line = Turtle()
score_L = Score((-100, 200))
score_R = Score((100, 200))
paddle_L = Paddle((-470, 0))
paddle_R = Paddle((470, 0))
ball = Ball()

screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

line.hideturtle()
line.shape("square")
line.speed("fastest")
line.color("white")
line.penup()
line.goto(x=0, y=265)
line.pendown()
line.right(90)
for num in range(15):
    line.forward(20)
    line.penup()
    line.forward(20)
    line.pendown()


screen.listen()
screen.onkey(fun=paddle_L.p1up, key="w")
screen.onkey(fun=paddle_L.p1down, key="s")
screen.onkey(fun=paddle_R.p1up, key="Up")
screen.onkey(fun=paddle_R.p1down, key="Down")

still_playing = True
while still_playing:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_down()

screen.exitonclick()
