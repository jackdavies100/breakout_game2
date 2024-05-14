from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import create_bricks
import pygame


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -350))  # Adjusted starting position
all_bricks = create_bricks()
ball = Ball(10)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50:
        ball.bounce_y()

    # Detect paddle misses
    if ball.ycor() < -280:  # If the ball reaches bottom of the screen
        ball.reset_position()
        scoreboard.l_point()

    # Detect collision with sides
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with bricks
    for brick in all_bricks:
        brick_center_x = brick.rect.x + brick.rect.width / 2
        brick_center_y = brick.rect.y + brick.rect.height / 2
        if abs(ball.xcor() - brick_center_x) < (ball.radius + brick.rect.width / 2) and \
                abs(ball.ycor() - brick_center_y) < (ball.radius + brick.rect.height / 2):
            ball.bounce_y()
            all_bricks.remove(brick)
            brick.kill()

screen.exitonclick()
