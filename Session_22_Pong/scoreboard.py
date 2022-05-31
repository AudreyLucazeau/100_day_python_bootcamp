from turtle import Screen, Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.j1 = 0
        self.j2 = 0

        self.goto(0, 250)