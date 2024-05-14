from turtle import Turtle

move_distance = 70

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(x=0, y=-280)

    def go_left(self):
        self.backward(move_distance)

    def go_right(self):
        self.forward(move_distance)
