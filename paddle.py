from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=0, y=-280)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(self.ycor(), new_x)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(self.ycor(), new_x)
