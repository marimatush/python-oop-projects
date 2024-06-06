"""
Manage canvas.
"""

from core.color import Color
import numpy as np
from PIL import Image


class Canvas:
    """
    Class for managing a canvas.
    """

    def __init__(self, width: int, height: int, color: Color):
        """
        Initialize a Canvas object.

        Args:
            width (int): The width of the canvas in pixels.
            height (int): The height of the canvas in pixels.
            color (str): The color of the canvas.

        """
        self.width: int = width
        self.height: int = height
        self.color: str = color

        self.image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.image[:] = [self.color.red, self.color.green, self.color.blue]

    def make(self, filepath: str):
        """
        Save the image to a file.

        Args:
            filepath (str): The path to save the image to.

        """
        image = Image.fromarray(self.image)
        image.save(filepath)
