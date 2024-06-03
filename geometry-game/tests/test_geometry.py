"""
Tests for geometry game classes.
"""

import unittest
from point import Point
from rectangle import Rectangle


class TestPointMethods(unittest.TestCase):
    """Test Point methods."""

    def test_point_falls_in_rectangle(self):
        """Test point falls in rectangle."""
        rec_point1 = Point(0, 0)
        rec_point2 = Point(5, 5)
        rectangle = Rectangle(rec_point1, rec_point2)
        point = Point(1, 2)

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


if __name__ == "__main__":
    unittest.main()
