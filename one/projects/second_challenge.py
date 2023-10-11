"""Coding Challenge Skeleton #2
"""


class Car:
    def __init__(self):
        self._speed = 0
        self._start_car = False

    def start_car(self):
        if self._start_car:
            raise Exception("car is on")
        else:
            self._start_car = True

    def turn_off_car(self):
        if self._start_car:
            self._start_car = False
        else:
            raise Exception("car is off")

    def add_speed(self):
        self._speed += 5

    def remove_speed(self):
        if self._speed <= 0:
            self._speed = 0
        else:
            self._speed -= 5

    def current_speed(self):
        return self._speed

    def stop(self):
        self._speed = 0

    def car_status(self):
        return self._start_car
