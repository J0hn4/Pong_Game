from turtle import Turtle

STARTING_POSITIONS = (380,0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.showturtle()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



    def move_paddle(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        if self.heading() != UP:
            self.setheading(UP)
        self.move_paddle()

    def down(self):
        if self.heading() != DOWN:
            self.setheading(DOWN)
        self.move_paddle()




