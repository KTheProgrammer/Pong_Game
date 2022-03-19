from turtle import Screen, Turtle

screen = Screen()
line = Turtle()
score1 = Turtle()
score2 = Turtle()

screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

score1.speed("fastest")
score1.hideturtle()
score1.penup()
score1.color("white")
score1.goto(x=-100, y=200)
score1.write("0", align="center", font=("Courier", 80, "normal"))

score2.speed("fastest")
score2.hideturtle()
score2.penup()
score2.color("white")
score2.goto(x=100, y=200)
score2.write("0", align="center", font=("Courier", 80, "normal"))

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


def p1up():
    paddle1.setheading(90)
    paddle1.forward(20)


def p1down():
    paddle1.setheading(270)
    paddle1.forward(20)


def p2up():
    paddle2.setheading(90)
    paddle2.forward(20)


def p2down():
    paddle2.setheading(270)
    paddle2.forward(20)


screen.listen()
screen.onkey(fun=p1up, key="w")
screen.onkey(fun=p1down, key="s")
screen.onkey(fun=p2up, key="Up")
screen.onkey(fun=p2down, key="Down")


paddle1 = Turtle(shape="square")
paddle1.speed("fastest")
paddle1.penup()
paddle1.right(90)
paddle1.color("white")
paddle1.goto(-470, 50)
paddle1.shapesize(stretch_len=5, stretch_wid=1)


paddle2 = Turtle(shape="square")
paddle2.speed("fastest")
paddle2.penup()
paddle2.right(90)
paddle2.color("white")
paddle2.goto(470, 50)
paddle2.shapesize(stretch_len=5, stretch_wid=1)

ball = Turtle(shape="square")
ball.color("white")
ball.goto(x=0, y=0)


screen.exitonclick()
