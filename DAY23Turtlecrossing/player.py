STARTING_POSITION = (0, -160)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 160
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('DarkOliveGreen3')
        self.shape('turtle')
        self.penup()
        self.start()
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)


    def start(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
