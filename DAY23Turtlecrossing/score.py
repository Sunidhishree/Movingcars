
import turtle
from turtle import Turtle
import random
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super(). __init__()
        self.s=0
        self.color("white")
        self.penup()
        self.goto(0,160)
        self.write(f"Level: {self.s}", align="center", font=(FONT))
        self.hideturtle()

    def increase(self):
        self.clear()
        self.s += 1
        self.write(f"Level: {self.s}", align="center", font=(FONT))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=(FONT))