from turtle import Turtle, Screen
import random
from snake import Snake

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed(0)

        self.positions_available=[(i,j) for i in range(-280,300,20) for j in range(-280,300,20)]
        self.positions_available.remove((-20,0))
        self.positions_available.remove((0,0))

        self.refresh()

    def update_positions_available(self, snake : Snake):
        try:
            self.positions_available.remove((round(snake.head.xcor()), round(snake.head.ycor())))
        except ValueError:
            print("")
        self.positions_available.append((round(snake.components[-1].xcor()), round(snake.components[-1].ycor())))

    def refresh(self):
        new_position = random.choice(self.positions_available)
        self.goto(new_position)

    def eat_food(self, snake : Snake):
        self.positions_available.remove((round(snake.components[-1].xcor()), round(snake.components[-1].ycor())))
        self.refresh()





