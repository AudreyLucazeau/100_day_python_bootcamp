from turtle import Turtle
import random
from grid_settings import SCREEN_HEIGHT, SCREEN_WIDTH
from paddle import Paddle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")

        self.penup()
        self.speed(0)
        self.reset()

    def move(self):
        self.forward(2)

    def wall_contact(self):
        if abs(round(self.ycor())) > SCREEN_HEIGHT/2-20:
            self.setheading(360-self.heading())

    def paddle_contact(self, paddle : Paddle):
        if self.distance(paddle) <50 and abs(self.xcor())>320:
            variation= self.ycor()-paddle.ycor()
            self.setheading(180-self.heading()-variation/5)


    def reset(self):
        self.goto(0,0)
        self.setheading(random.randrange(-50, 50, 1))