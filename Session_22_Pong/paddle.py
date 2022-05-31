from turtle import Turtle
from grid_settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.speed(0)

    def move_up(self):
        if self.ycor() < SCREEN_HEIGHT/2 -50:
            self.forward(10)

    def move_down(self):
        if self.ycor() > -SCREEN_HEIGHT/2 + 50:
            self.back(10)

    def on_grid(self):
        return abs(self.ycor())<SCREEN_HEIGHT-20

