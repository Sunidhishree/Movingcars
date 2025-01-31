from turtle import Turtle
import random
locations=[-130,-90,-50,-10,30,70,110,150]

COLORS = ["indianred", "orange", "yellow", "coral", "CadetBlue1", "plum","orchid4","Peachpuff","pink","SkyBlue3","turquoise"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars=[]
        self.speed=STARTING_MOVE_DISTANCE

    def Create(self):
        rand=random.randint(1,7)
        if rand==1:
            new = Turtle('square')
            new.shapesize(1, 2)
            new.penup()
            new.color(random.choice(COLORS))
            new.goto(300, random.choice(locations))
            self.cars.append(new)

    def move(self):
        for i in self.cars:
            i.backward(self.speed)

    def levelup(self):
        self.speed+=MOVE_INCREMENT