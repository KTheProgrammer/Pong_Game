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
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(paddle_R) < 50 and ball.xcor() > 320 or ball.distance(paddle_L) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect pass wall to score
    if ball.xcor() > 500:
        score_L.add_score()
        ball.goto(0, 0)
        ball.bounce_x()
    elif ball.xcor() < -500:
        score_R.add_score()
        ball.goto(0, 0)
        ball.bounce_x()

    # Determine Winner
    if score_L.scored == 10:
        score_L.end_game("left")
        still_playing = False
    elif score_R.scored == 10:
        score_R.end_game("right")
        still_playing = False

screen.exitonclick()
