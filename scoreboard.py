from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="Game Over!!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
