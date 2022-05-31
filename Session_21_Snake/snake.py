from turtle import Turtle, Screen

global TURTLE_SIZE
TURTLE_SIZE = 20


class Snake:

    def __init__(self):
        self.components = []
        self.create_snake()
        self.length = len(self.components)
        self.head = self.components[0]

    def create_snake(self):
        for i in range(3):
            new_square = Turtle(shape="square")
            new_square.penup()
            new_square.speed(0)
            new_square.goto(-i * TURTLE_SIZE, 0)
            self.components.append(new_square)

    def move(self):
        for index in range(len(self.components) - 1, 0, -1):
            self.components[index].goto(self.components[index - 1].pos())
        self.head.forward(20)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def is_eating_tail(self):
        for square in self.components[1:]:
            if self.head.distance(square) < 10:
                return True
        return False

    def is_out_of_grid(self, screen: Screen):
        if abs(self.head.position()[0]) >= screen.window_width()/2 or \
                abs(self.head.position()[1]) >= screen.window_height()/2:
            return True

        return False

    def get_positions(self):
        positions = []
        for square in self.components :
            positions.append(list(square.position()))
        return positions

    def eat_food(self):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.speed(0)
        new_square.goto(self.components[-1].position())
        self.move()
        self.components.append(new_square)



