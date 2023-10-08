import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.making_cars()

    def making_cars(self):
        make_slow_the_process = random.randint(1,5)
        if make_slow_the_process == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            rand = random.randint(-280,280)
            car.setheading(180)
            car.shapesize(stretch_wid=0.6, stretch_len=1.3)
            car.color(random.choice(COLORS))
            car.goto(310,rand)
            self.all_cars.append(car)

    def moving_cars(self):
        for car in self.all_cars:
            rand = random.randint(0, 10)
            car.forward(rand)
