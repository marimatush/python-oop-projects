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
        # Determine the min and max x and y values for the rectangle
        min_x = min(rectangle.point1.x, rectangle.point2.x)
        max_x = max(rectangle.point1.x, rectangle.point2.x)
        min_y = min(rectangle.point1.y, rectangle.point2.y)
        max_y = max(rectangle.point1.y, rectangle.point2.y)

        # Check if the point lies within the rectangle bounds
        return min_x <= self.x <= max_x and min_y <= self.y <= max_y

    def distance_from_point(self, point):
        """Calculate distance from a point."""
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class GuiPoint(Point):
    """Provides GUI for a point."""

    def draw(self, canvas, size=5, color="red"):
        """Draws a point on canvas."""
        # Go to a starting coordinate
        canvas.penup()
        canvas.goto(self.x, self.y)

        # Draw a dot
        canvas.pendown()
        canvas.dot(size, color)
