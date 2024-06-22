from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")  # Set the color of the ball to white
        self.shape("circle")  # Set the shape of the ball to a circle
        self.penup()  # Lift the pen to avoid drawing lines
        self.x_move = 10  # Initial movement in the x direction
        self.y_move = 10  # Initial movement in the y direction
        self.move_speed = 0.1  # Initial speed of the ball

    def move(self):
        """Move the ball to a new position based on its current position and movement increments."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the y direction of the ball and increase its speed."""
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        """Reverse the x direction of the ball and increase its speed."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the ball to the center of the screen and reset its speed."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
