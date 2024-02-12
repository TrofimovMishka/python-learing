COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 8

import random
from turtle import Turtle


class CarManager:

    def __init__(self):
        self.cars = []

    def go(self):
        for car in self.cars:
            car.fd(MOVE_INCREMENT)

    def add_car(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.turtlesize(1, 2)
        car.penup()
        y = random.randint(-250, 250)
        car.goto(300, y)
        car.setheading(180)

        self.cars.append(car)

    def delete_unbound_cars(self, max_height):
        for car in self.cars:
            if car.xcor() < max_height / 2 * -1:
                self.cars.remove(car)

    def detect_collision(self, obj):
        for car in self.cars:
            if car.distance(obj) < 23:
                return True
        return False

    def increase_speed(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT += 5
