from math import pi
from src.figure import Figure


class Circle(Figure):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("r must be greater than 0")
        self.r = r

    def get_area(self):
        return pi * (self.r ** 2)

    def get_perimeter(self):
        return 2 * pi * self.r
