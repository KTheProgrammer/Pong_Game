from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(cords)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def p1up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 240:
            self.goto(self.xcor(), new_y)

    def p1down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -240:
            self.goto(self.xcor(), new_y)
