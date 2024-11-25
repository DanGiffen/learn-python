from turtle import Turtle

PADDLE_COLOUR = "white"
PADDLE_SHAPE = "square"
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOUR)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(start_position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
