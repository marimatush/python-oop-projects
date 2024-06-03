"""
Class geometry rectangle.
"""


class Rectangle:
    """Class geomentry rectangle."""

    def __init__(self, point1, point2):
        """Initialize with two diagonal points"""
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return (
            "Rectangular with coordinates"
            f" ({self.point1.x}, {self.point1.y})"
            f" ({self.point2.x}, {self.point2.y})"
        )

    def area(self):
        """Calculate area of rectangle."""
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)
