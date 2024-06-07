"""
Manage shapes.
"""

from .color import Color
from .canvas import Canvas


class Rectangle:
    """
    Class for managing rectangles.
    """

    def __init__(self, x: int, y: int, width: int, height: int, color: Color) -> None:
        """
        Initialize a rectangle object.

        Args:
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            width (int): The width of the rectangle in pixels.
            height (int): The height of the rectangle in pixels.
            color (str): The color of the rectangle.

        """
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.color: Color = color

    def draw(self, canvas: Canvas) -> None:
        """
        Draw the rectangle on the canvas.

        Args:
            canvas (Canvas): The canvas to draw on.

        """
        canvas.image[self.y : self.y + self.height, self.x : self.x + self.width] = [
            self.color.red,
            self.color.green,
            self.color.blue,
        ]


class Square(Rectangle):
    """
    Class for managing squares.
    """

    def __init__(self, x: int, y: int, side: int, color: Color):
        """
        Initialize a square object.

        Args:
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            side (int): The side length of the square in pixels.
            color (str): The color of the square.

        """
        super().__init__(x, y, side, side, color)
