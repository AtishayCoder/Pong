from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.position = position

    def up(self):
        y = self.ycor() + 20
        self.goto(self.position[0], y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.position[0], y)
