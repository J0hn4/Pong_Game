from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_other_way(self):
        self.x_move *= -1

    def ball_reset(self):
        self.hideturtle()
        self.goto(0, 0)
        self.bounce_other_way()
        self.showturtle()

    def increase_speed(self):
        self.move_speed *= 0.5

    # def start_random_move(self):
    #     self.right(random.randint(0, 360))
    #     while self.xcor() < 290 or self.xcor() > -290 or self.ycor() < 390 or self.ycor() < 390:
    #         self.forward(20)

    # def move_right(self):
    #     new_x = self.xcor() + 10
    #     self.goto(new_x,self.ycor())
    #
    #
    # def move_left(self):
    #     new_x = self.xcor() - 10
    #     self.goto(new_x,self.ycor())
    #
    # def move_up(self):
    #     new_y = self.ycor() + 10
    #     self.goto(self.xcor(),new_y)
    #
    #
    # def move_down(self):
    #     new_y = self.ycor() - 10
    #     self.goto(self.xcor(),new_y)
    #
    # def move(self):
    #     if self.ycor() == 280:
    #         self.move_down()


    # def bounce_up(self):
    #     if self.ycor() == -280:
    #         new_x = self.xcor() - 20
    #         new_y = self.ycor() + 20
    #
    # def bounce(self):
    #     if self.ycor() == 290:
    #         new_x = self.xcor() - 20
    #         new_y = self.ycor() + 20
    #         self.goto(new_x, new_y)
    #     elif self.ycor() == -280:
    #         new_x = self.xcor() - 20
    #         new_y = self.ycor() + 20




            # or self.xcor() > -290 or self.ycor() < 390 or self.ycor() < 390: