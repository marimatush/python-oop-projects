"""
Tests for geometry game classes.
"""

import unittest
from unittest.mock import Mock
from geometry_game.point import Point, GuiPoint
from geometry_game.rectangle import Rectangle, GuiRectangle


class TestPointMethods(unittest.TestCase):
    """Test Point methods."""

    def test_point_falls_in_rectangle_lower_to_upper_coordinates(self):
        """Test point falls in rectangle defined with lower to upper coordinates."""
        rec_point1 = Point(0, 0)
        rec_point2 = Point(5, 5)
        rectangle = Rectangle(rec_point1, rec_point2)
        point = Point(1, 2)

        point_falls_in_rec = point.falls_in_rectangle(rectangle)
        self.assertTrue(point_falls_in_rec)

    def test_point_falls_in_rectangle_upper_to_lower_coordinates(self):
        """Test point falls in rectangle defined with upper to lower coordinates."""
        rec_point1 = Point(10, 6)
        rec_point2 = Point(3, 2)
        rectangle = Rectangle(rec_point1, rec_point2)
        point = Point(5, 4)

        point_falls_in_rec = point.falls_in_rectangle(rectangle)
        self.assertTrue(point_falls_in_rec)

    def test_point_does_not_fall_in_rectangle(self):
        """Test point does not fall in rectangle."""
        rec_point1 = Point(0, 0)
        rec_point2 = Point(5, 5)
        rectangle = Rectangle(rec_point1, rec_point2)
        point = Point(10, 20)

        point_falls_in_rec = point.falls_in_rectangle(rectangle)
        self.assertFalse(point_falls_in_rec)

    def test_distance_from_point(self):
        """Test distance between two points."""
        point1 = Point(0, 0)
        point2 = Point(3, 4)

        expected_distance = 5.0  # As per the 3-4-5 triangle rule
        calculated_distance = point1.distance_from_point(point2)

        self.assertAlmostEqual(calculated_distance, expected_distance, places=7)

    def test_draw_point(self):
        """Test drawing a point."""
        canvas = Mock()

        # Creating a GuiPoint instance
        point = GuiPoint(50, 50)

        # Calling the draw method
        point.draw(canvas)

        # Asserting canvas method calls with default parameters
        canvas.penup.assert_called_once()
        canvas.goto.assert_called_once_with(50, 50)
        canvas.pendown.assert_called_once()
        canvas.dot.assert_called_once_with(5, "red")


class TestRectangleMethods(unittest.TestCase):
    """Test Rectangle methods."""

    def test_area(self):
        """Test area of a rectangle."""
        rec_point1 = Point(0, 0)
        rec_point2 = Point(5, 5)
        rectangle = Rectangle(rec_point1, rec_point2)

        expected_erea = 25  # 5 * 5
        calculated_area = rectangle.area()

        self.assertEqual(calculated_area, expected_erea)

    def test_draw_rectangle(self):
        """Test drawing a rectangle."""
        canvas = Mock()

        # Creating a GuiRectangle instance
        point1 = Point(0, 0)
        point2 = Point(100, 100)
        rectangle = GuiRectangle(point1, point2)

        # Calling the draw method
        rectangle.draw(canvas)

        # Asserting canvas method calls with custom parameters
        canvas.penup.assert_called_once()
        canvas.goto.assert_called_once_with(0, 0)
        canvas.pendown.assert_called_once()
        canvas.left.assert_called_with(90)


if __name__ == "__main__":
    unittest.main()
