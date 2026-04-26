import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if car.level != player.level:
        car.increase_speed()
        car.level = player.level
        scoreboard.level = player.level
        scoreboard.update_scoreboard()

    car.create_car()
    car.move_cars()

    for each_car in car.list_of_cars:
        if player.distance(each_car) < 20:
            game_is_on = False
            scoreboard.game_over()
    
screen.exitonclick()
