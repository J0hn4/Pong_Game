from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer()

r_paddle = Paddle((380,0))
l_paddle = Paddle((-380,0))
ball =Ball()
scoreboard = ScoreBoard()

#ball.start_random_move()



screen.listen()



screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_other_way()

    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.add_point_l()
        ball.increase_speed()

    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.add_point_r()
        ball.increase_speed()


# screen.update()

screen.exitonclick()



# y_direction = ball.move_up()
#     x_direction = ball.move_right()
#     if ball.ycor() == 280:
#         y_direction = ball.move_down()
#     elif ball.ycor()  == -280:
#         y_direction = ball.move_up()
#     elif ball.distance(r_paddle) < 15:
#         x_direction = ball.move_left()
#     elif ball.distance((l_paddle)) < 15:
#         x_direction = ball.move_right()