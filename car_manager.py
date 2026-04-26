from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.list_of_cars = []
        self.level = 1
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            y_cord = randint(-250, 250)
            new_car = Turtle("square")
            new_car.turtlesize(1, 2, 0)
            new_car.penup()
            new_car.goto(310, y=y_cord)
            new_car.color(choice(COLORS))
            self.list_of_cars.append(new_car)

    def move_cars(self):
        for car in self.list_of_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
