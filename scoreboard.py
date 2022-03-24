from turtle import Turtle


class Score:
    def __init__(self, area):
        self.score = Turtle()
        self.scored = 0
        self.score.hideturtle()
        self.score.penup()
        self.score.speed("fastest")
        self.score.color("white")
        self.score.goto(area)
        self.score.write("0", align="center", font=("Courier", 80, "normal"))

    def add_score(self):
        self.scored += 1
        self.score.clear()
        self.score.write(f"{self.scored}", align="center", font=("Courier", 80, "normal"))

    def end_game(self, side):
        self.score.goto(0, 0)
        self.score.write(f"Person on {side} side Won!!!", align="center", font=("Courier", 40, "normal"))
