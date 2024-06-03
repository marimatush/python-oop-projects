"""
Geometry game:
    Give a rectangle with random coordinates for their lower-left and upper-right
    corners.
    User guessing points inside a rectangle.
    User guessing area of a rectangle.
"""

from random import randint
from point import Point, GuiPoint
from rectangle import GuiRectangle
import turtle

# Create a rectangle
rectangle = GuiRectangle(
    Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400))
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

# Get imputs from the user
user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside the rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your areas was off by: ", abs(rectangle.area() - user_area))

canvas = turtle.Turtle()

# Draw a rectangle
rectangle.draw(canvas=canvas)

# Draw a point
user_point.draw(canvas=canvas)

turtle.done()
