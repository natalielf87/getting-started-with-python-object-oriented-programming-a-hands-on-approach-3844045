"""
A class for representing a circle
"""
import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def display_circumrefence(self):
        print(f"Circumference is {round(2 * math.pi * self.radius, 2)}")

    def display_area(self):
        print(f"Area is {round(math.pi * self.radius ** 2, 2)}")


if __name__ == "__main__":
    circle1 = Circle(5)
    circle1.display_circumrefence()
    circle1.display_area()
