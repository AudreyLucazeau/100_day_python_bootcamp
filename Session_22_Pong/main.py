from turtle import Turtle, Screen
import time
from grid_settings import SCREEN_HEIGHT, SCREEN_WIDTH
from paddle import Paddle
from ball import Ball
from scoreboard import Score

play_screen = Screen()
play_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
play_screen.tracer(0)

paddle1 = Paddle()
paddle1.goto(SCREEN_WIDTH/2-50, 0)
paddle2 = Paddle()
paddle2.goto(-SCREEN_WIDTH/2+50, 0)

play_screen.listen()
play_screen.onkey(paddle1.move_down, "Down")
play_screen.onkey(paddle1.move_up, "Up")
play_screen.onkey(paddle2.move_down, "s")
play_screen.onkey(paddle2.move_up, "w")

game_in_on = True

my_ball = Ball()
play_screen.tracer(1)

score = Score()

while game_in_on:
    my_ball.move()
    my_ball.paddle_contact(paddle1)
    my_ball.wall_contact()
    my_ball.paddle_contact(paddle2)
    if my_ball.xcor()>SCREEN_WIDTH-20 :
        score.j1 +=1
        my_ball.goto(0,0)
        score.clear()
    if my_ball.xcor()<-SCREEN_WIDTH+20 :
        score.clear()
        score.j2 +=1
        my_ball.goto(0,0)

    score.write(f"{score.j1} -- {score.j2}", move=False, align="left", font=("Arial", 8, "normal"))


play_screen.exitonclick()
