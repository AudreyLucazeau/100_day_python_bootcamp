import time
from turtle import Screen, Turtle
import snake as sn
from food import Food

WIDTH = 620
HEIGHT = 620

my_screen = Screen()
food = Food()
my_screen.setup(WIDTH, HEIGHT)

my_screen.title("My Snake Game")

my_snake = sn.Snake()

my_screen.listen()
my_screen.onkey(my_snake.move_right, "Right")
my_screen.onkey(my_snake.move_up, "Up")
my_screen.onkey(my_snake.move_down, "Down")
my_screen.onkey(my_snake.move_left, "Left")

compteur = 0
while not(my_snake.is_eating_tail() or my_snake.is_out_of_grid(my_screen)) :
    time.sleep(0.2)
    my_snake.move()
    food.update_positions_available(my_snake)
    if my_snake.head.distance(food) < 10:
        food.eat_food(my_snake)
        my_snake.eat_food()
        food.update_positions_available(my_snake)
    my_screen.update()

end_game = Turtle()
end_game.hideturtle()
end_game.write("GAME OVER", align = "center")


my_screen.exitonclick()
