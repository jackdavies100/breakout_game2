from turtle import Turtle

MOVE_DIST = 2

class Ball(Turtle):

    def __init__(self, radius):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move_dist = MOVE_DIST
        self.y_move_dist = MOVE_DIST
        self.reset()

    def move(self):
        new_x = self.xcor() + self.x_move_dist
        new_y = self.ycor() + self.y_move_dist
        self.goto(x=new_x, y=new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move_dist *= -1

        if y_bounce:
            self.y_move_dist *= -1
    def reset(self):
        self.goto(x=0, y=-240)
        self.y_move_dist = 10
