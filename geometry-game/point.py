"""
Class geometry point.
"""


class Point:
    """Class geometry point."""

    def __init__(self, x, y):
        """Initialize with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point with coordinates x: {self.x}, y: {self.y}"

    def falls_in_rectangle(self, rectangle):
        """Check if the point falls in a rectangel."""
        if (
            rectangle.point1.x < self.x < rectangle.point2.x
            and rectangle.point1.y < self.y < rectangle.point2.y
        ):
            return True
        else:
            return False

    def distance_from_point(self, point):
        """Calculate distance from a point."""
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
