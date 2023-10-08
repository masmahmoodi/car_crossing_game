import time
from turtle import Screen
from player import  Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
level = Scoreboard()
screen.listen()
screen.onkey(player.moving_player, "Up")
on = True
c = 0.1
while on:
    time.sleep(c)
    screen.update()
    car_manager.making_cars()
    car_manager.moving_cars()
    if player.player_1[0].ycor() > 280:
        player.restarting_player()
        c *= 0.7
        level.increasing_level()
    for car in car_manager.all_cars:
        if car.distance(player.player_1[0])<15:
            on = False
            level.game_over()



screen.exitonclick()