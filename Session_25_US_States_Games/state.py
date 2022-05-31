from turtle import Turtle
import pandas
from time import sleep

class State(Turtle):

    def __init__(self, name, x, y ):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(x,y)
        self.id = name

    def reveal(self):
        self.clear()
        self.write(self.id, align="center", font =('Arial', 8, 'normal'))

    def emphasize(self):
        self.clear()
        self.write(self.id.upper(), align="center", font =('Arial', 12, 'normal'))
        sleep(0.5)
        self.reveal()


