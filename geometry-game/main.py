"""
Geometry game:
    Give a rectangle with random coordinates for their lower-left and upper-right
    corners.
    User guessing points inside a rectangle.
    User guessing area of a rectangle.
"""

from random import randint
from point import Point
from rectangle import Rectangle

rectangle = Rectangle(
    Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19))
)

print(
    "Rectangle coordinates:",
    rectangle.point1.x,
    ",",
    rectangle.point1.y,
    "and",
    rectangle.point2.x,
    ",",
    rectangle.point2.y,
)

user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

print("Your point was inside the rectangle: ", user_point.falls_in_rectangle(rectangle))

print("Your areas was off by: ", abs(rectangle.area() - user_area))
