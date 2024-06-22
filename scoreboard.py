from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")  # Set the color of the scoreboard text to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.hideturtle()  # Hide the turtle cursor
        self.l_score = 0  # Initialize left player's score
        self.r_score = 0  # Initialize right player's score
        self.update_scoreboard()  # Display the initial score

    def update_scoreboard(self):
        """Update the scoreboard with the current scores."""
        self.clear()  # Clear the previous score
        self.goto(-100, 200)  # Position for left player's score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)  # Position for right player's score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increase the left player's score by one and update the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increase the right player's score by one and update the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()
