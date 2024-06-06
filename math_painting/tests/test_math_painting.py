"""
Tests for the math painting module.
"""

import unittest

import numpy as np
from math_painting.core.shape import Rectangle, Square
from math_painting.core.canvas import Canvas
from math_painting.core.color import Color


class TestColor(unittest.TestCase):
    """
    Tests for the color module.
    """

    def test_color_init(self):
        """
        Test the Color class.
        """
        new_color = Color(1, 2, 3)
        self.assertEqual(new_color.red, 1)
        self.assertEqual(new_color.green, 2)
        self.assertEqual(new_color.blue, 3)

    def test_color_init_exception(self):
        """
        Test the Color class.
        """
        with self.assertRaises(ValueError):
            Color(256, 2, 3)

        with self.assertRaises(ValueError):
            Color(-1, 2, 3)

        with self.assertRaises(ValueError):
            Color(1, 256, 3)

        with self.assertRaises(ValueError):
            Color(1, -1, 3)

        with self.assertRaises(ValueError):
            Color(1, 2, 256)


class TestRectangle(unittest.TestCase):
    """
    Tests for the Rectangle module.
    """

    def test_rectangle_init(self):
        """
        Test the Rectangle class.
        """
        color = Color(10, 20, 30)
        new_rectangle = Rectangle(1, 2, 3, 4, color)
        self.assertEqual(new_rectangle.x, 1)
        self.assertEqual(new_rectangle.y, 2)
        self.assertEqual(new_rectangle.width, 3)
        self.assertEqual(new_rectangle.height, 4)
        self.assertEqual(new_rectangle.color, color)

    def test_Rectangle_draw(self):
        """Test the draw method of the rectangle class."""
        rectangle_color = Color(255, 0, 0)
        canvas = Canvas(100, 100, Color(0, 0, 0))
        new_rectangle = Rectangle(
            x=10, y=10, width=10, height=10, color=rectangle_color
        )
        new_rectangle.draw(canvas)


class TestSquare(unittest.TestCase):
    """
    Tests for the Square module.
    """

    def test_Square_init(self):
        """
        Test the Square class.
        """
        color = Color(10, 20, 30)
        new_Square = Square(1, 2, 3, color)
        self.assertEqual(new_Square.x, 1)
        self.assertEqual(new_Square.y, 2)
        self.assertEqual(new_Square.width, 3)
        self.assertEqual(new_Square.height, 3)
        self.assertEqual(new_Square.color, color)

    def test_Square_draw(self):
        """Test the draw method of the Square class."""
        Square_color = Color(255, 0, 0)
        canvas = Canvas(100, 100, Color(0, 0, 0))
        new_Square = Square(x=10, y=10, side=10, color=Square_color)
        new_Square.draw(canvas)


class TestCanvas(unittest.TestCase):
    """
    Tests for the canvas module.
    """

    def test_canvas_init(self):
        """
        Test the Canvas class.
        """
        canvas_color = Color(0, 0, 0)  # black
        new_canvas = Canvas(100, 100, canvas_color)
        self.assertEqual(new_canvas.width, 100)
        self.assertEqual(new_canvas.height, 100)
        self.assertEqual(new_canvas.color, canvas_color)

        canvas_image = np.zeros((100, 100, 3), dtype=np.uint8)
        canvas_image[:] = [0, 0, 0]
        self.assertTrue((new_canvas.image == canvas_image).all())


if __name__ == "__main__":
    unittest.main()
