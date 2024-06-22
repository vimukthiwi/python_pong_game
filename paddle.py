from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle to the desired size
        self.goto(position)  # Position the paddle at the specified location

    # Paddle movement functions
    def up(self):
        """Move the paddle up by 20 units."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Move the paddle down by 20 units."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
