from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, current_score):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def update_score(self, current_score):
        self.clear()
        self.write(f"Score: {current_score}", False, align=ALIGNMENT, font=FONT)

