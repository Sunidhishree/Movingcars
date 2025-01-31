import time
from turtle import Screen
from player import Player
from carmanager import CarManager
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.tracer(0)
player=Player()
carmanager=CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(player.up, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.Create()
    carmanager.move()
    for i in carmanager.cars:
        if player.distance(i)<20:
            game_is_on=False
            score.game_over()
    if player.finish():
        player.start()
        carmanager.levelup()