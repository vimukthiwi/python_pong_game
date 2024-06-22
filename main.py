from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create a Screen object
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turn off the screen updates

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Keyboard bindings for right paddle
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Keyboard bindings for left paddle
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Game loop flag
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the ball
    screen.update()  # Update the screen
    ball.move()  # Move the ball

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()  # Left player scores a point

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()  # Right player scores a point

# Wait for a click on the screen to exit
screen.exitonclick()
